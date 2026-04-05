from urllib.parse import quote


def build_favicon_data_uri() -> str:
    svg = """
    <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
      <rect width="64" height="64" rx="16" fill="#102029"/>
      <g transform="translate(8 8) scale(2)">
        <path d="M0 0h24v24H0z" fill="none"/>
        <path fill="#f6f1e7" d="M12 11.55C9.64 9.35 6.48 8 3 8v11c3.48 0 6.64 1.35 9 3.55 2.36-2.19 5.52-3.55 9-3.55V8c-3.48 0-6.64 1.35-9 3.55zM12 8c1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3 1.34 3 3 3z"/>
      </g>
    </svg>
    """.strip()
    return f'data:image/svg+xml;utf8,{quote(svg)}'
