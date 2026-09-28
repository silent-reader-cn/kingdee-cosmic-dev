# 高新项目支出-rdem_fzz_gx_zc

## 高新项目支出-主表 t_rdem_fzz_gx_zc

- **表名称：** 高新项目支出-主表
- **表名：** t_rdem_fzz_gx_zc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsjfy | 设计费用 | numeric | 23 | 2 | √ | 0 | 设计费用 |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fwtjwwbyjkffy | 委托境外外部研究开发费用 | numeric | 23 | 2 | √ | 0 | 委托境外外部研究开发费用 |
| 5 | fzjfyycqdtfy | 折旧费用与长期待摊费用 | numeric | 23 | 2 | √ | 0 | 折旧费用与长期待摊费用 |
| 6 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 7 | fqtfy | 其他费用 | numeric | 23 | 2 | √ | 0 | 其他费用 |
| 8 | fzjtrfy | 直接投入费用 | numeric | 23 | 2 | √ | 0 | 直接投入费用 |
| 9 | fzbtsfyysyfy | 装备调试费用与试验费用 | numeric | 23 | 2 | √ | 0 | 装备调试费用与试验费用 |
| 10 | fwxzctxfy | 无形资产摊销费用 | numeric | 23 | 2 | √ | 0 | 无形资产摊销费用 |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fryrgfy | 人员人工费用 | numeric | 23 | 2 | √ | 0 | 人员人工费用 |
| 13 | fwcqk | 完成情况 | varchar | 50 |  | √ | ' ' | 完成情况 |
| 14 | fsbxm | 申报项目基础资料 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 15 | fwtjnwbyjkffy | 委托境内外部研究开发费用 | numeric | 23 | 2 | √ | 0 | 委托境内外部研究开发费用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzz_gx_zc_m0 |  | fwcqk |
| 2 | pk_rdem_fzz_gx_zc |  | fid |
