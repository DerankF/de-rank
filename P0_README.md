# 帝意排行榜 · 公信力系统 P0 骨架（2026-11-22）

本目录为公信力系统 P0 自动化产物（路线图见 `D:/WorkBuddy/Claw/media_engine/evo_loop/system/04_落地路线图.md`）。**只新增文件，不改动任何现有站点页面**。

## 已建（AI 自动，P0-1~7）
| 项 | 文件 | 状态 |
|---|---|---|
| P0-1 仓库骨架 | `/rules /scripts /snapshots /corrections /methodology` | ✅ |
| P0-2 数据规则 | `rules/rules.json` | ✅ 参数化，阈值标 pending |
| P0-3 复算脚本 | `scripts/recompute.py` + `scripts/tests/sample.csv` | ✅ 跑通，diff 自检 |
| P0-4 指标元数据 | `methodology/indicators.json` | ✅ D-01~D-09 对齐已公开口径 |
| P0-5 JSON-LD/Fact Block | `scripts/jsonld_templates.json` + `factblock_template.txt` | ✅ 四类 schema 模板 |
| P0-6 llms/独立性/更正骨架 | `llms.txt`(已增补) + `methodology/independence.md` + `corrections/index.md` | ✅ 草案标记 |
| P0-7 changelog | `changelog.json` | ✅ 空日志机制 |

## 待真人（P0-8~10，AI 不代办）
- **P0-8** 编辑委员会逐条定稿 18→9 项指标定义/权重/归一化，替换 rules.json 与 indicators.json 中 `pending=true` / `PLACEHOLDER_`。
- **P0-9** 主办方签署独立性条款（`independence.md` 签署栏）。
- **P0-10** 扫码/站长验证：GitHub Pages 部署、搜索引擎站长验证、IndexNow key 等（涉及身份，必须本人）。

## 关键约束
- 所有口径沿用已公开 `scoring-weights_20261111.csv`（帝意指数=民意60%+专业40%），**未擅自改口径**。
- 未定稿参数一律标 `pending=true`，占位符标 `PLACEHOLDER_`，不伪装成已验证。
- 更正日志、独立性条款均为草案/空，未发布前不构成正式承诺。
