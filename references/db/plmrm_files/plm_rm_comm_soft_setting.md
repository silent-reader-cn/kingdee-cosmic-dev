# 公共配置-软件-plm_rm_comm_soft_setting

## 公共配置-软件-主表 t_plm_rm_comm_soft_set

- **表名称：** 公共配置-软件-主表
- **表名：** t_plm_rm_comm_soft_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 3 | firdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 4 | fsr | SR系统需求 | bpchar | 1 |  | √ | '1' | SR系统需求 |
| 5 | fus | US用户故事 | bpchar | 1 |  | √ | '1' | US用户故事 |
| 6 | fothernamepb | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 7 | fpbdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 8 | fsrdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 9 | fbasedatafieldsf | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 10 | fsfdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 11 | fir | IR初始需求 | bpchar | 1 |  | √ | '1' | IR初始需求 |
| 12 | ftextfield | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fcombofieldpb | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 14 | fbasedatafieldus | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 15 | fbasedatafieldsr | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 16 | fpb | PB核心问题 | bpchar | 1 |  | √ | '1' | PB核心问题 |
| 17 | fbasedatafieldir | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 18 | fcombofieldsr | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 19 | fcombofieldus | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 20 | fothernamesf | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 21 | fbasedatafieldpb | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 22 | fcombofieldir | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 23 | fcombofieldsf | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 24 | fothernameus | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 25 | fothernamesr | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 26 | fsf | SF系统特性 | bpchar | 1 |  | √ | '1' | SF系统特性 |
| 27 | fothernameir | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_comm_soft_set_m0 |  | fcombofieldus |
| 2 | pk_plm_rm_comm_soft_set |  | fid |
