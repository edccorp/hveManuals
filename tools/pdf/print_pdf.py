"""Render each manual HTML to PDF via Chromium DevTools, with header/footer."""
import base64, json, os, subprocess, sys, time, urllib.request, socket, glob
import websocket

CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium')
HTMLDIR = sys.argv[1]
PDFDIR  = sys.argv[2]
os.makedirs(PDFDIR, exist_ok=True)

def free_port():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p

PORT = free_port()
proc = subprocess.Popen(
    [CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
     f'--remote-debugging-port={PORT}', '--remote-allow-origins=*',
     '--allow-file-access-from-files', '--font-render-hinting=none',
     'about:blank'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for _ in range(80):
    try:
        v = json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json/version', timeout=1))
        break
    except Exception:
        time.sleep(0.25)
else:
    print('chrome did not start'); proc.kill(); sys.exit(1)

HEADER = ('<div style="font:8pt Georgia,serif;color:#777;width:100%;'
          'padding:0 14mm;border-bottom:.4pt solid #ccc;margin-bottom:2mm;">'
          '<span style="float:left">HVE &mdash; TITLE</span>'
          '<span style="float:right">Engineering Dynamics Company</span></div>')
FOOTER = ('<div style="font:8pt Georgia,serif;color:#777;width:100%;'
          'padding:0 14mm;text-align:center;">'
          'Page <span class="pageNumber"></span> of <span class="totalPages"></span>'
          '</div>')

results = []
for src in sorted(glob.glob(os.path.join(HTMLDIR, '*.html'))):
    name = os.path.splitext(os.path.basename(src))[0]
    tab = json.load(urllib.request.urlopen(
        urllib.request.Request(f'http://127.0.0.1:{PORT}/json/new?about:blank', method='PUT')))
    ws = websocket.create_connection(tab['webSocketDebuggerUrl'], timeout=600,
                                     suppress_origin=True)
    mid = [0]
    def send(method, params=None, wait=True):
        mid[0] += 1
        ws.send(json.dumps({'id': mid[0], 'method': method, 'params': params or {}}))
        if not wait: return None
        while True:
            m = json.loads(ws.recv())
            if m.get('id') == mid[0]:
                return m
    send('Page.enable')
    send('Page.navigate', {'url': 'file://' + os.path.abspath(src)})
    # wait for load event
    deadline = time.time() + 240
    while time.time() < deadline:
        m = json.loads(ws.recv())
        if m.get('method') == 'Page.loadEventFired':
            break
    time.sleep(2.5)   # let MathML/layout settle
    title = name.replace('-', ' ')
    r = send('Page.printToPDF', {
        'printBackground': True, 'preferCSSPageSize': True,
        'displayHeaderFooter': True,
        'headerTemplate': HEADER.replace('TITLE', title),
        'footerTemplate': FOOTER,
        'marginTop': 0.75, 'marginBottom': 0.6,
        'marginLeft': 0.7, 'marginRight': 0.7,
    })
    if 'result' not in r:
        print(f'  {name}: FAILED {r.get("error")}')
        ws.close(); continue
    data = base64.b64decode(r['result']['data'])
    out = os.path.join(PDFDIR, name + '.pdf')
    open(out, 'wb').write(data)
    results.append((name, len(data)))
    ws.close()
    urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json/close/' + tab['id']).read()
    print(f'  {name:<24} {len(data)/1e6:6.2f} MB')

proc.terminate()
print(f'\n{len(results)} PDFs written to {PDFDIR}')
