# 公共配置-plm_rm_comm_pack_setting

## 公共配置-主表 t_plm_rm_comm_pack_set

- **表名称：** 公共配置-主表
- **表名：** t_plm_rm_comm_pack_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsoftprdus | US | bpchar | 1 |  | √ | '0' | US |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fsoftprdsr | SR | bpchar | 1 |  | √ | '0' | SR |
| 4 | felecmrdir | IR | bpchar | 1 |  | √ | '0' | IR |
| 5 | fsoftmrdpb | PB | bpchar | 1 |  | √ | '0' | PB |
| 6 | fsoftmrdrr | RR | bpchar | 1 |  | √ | '1' | RR |
| 7 | fcombofieldprd | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 8 | fsoftprdir | IR | bpchar | 1 |  | √ | '0' | IR |
| 9 | felecprdsf | SF | bpchar | 1 |  | √ | '0' | SF |
| 10 | felecmrdsr | SR | bpchar | 1 |  | √ | '0' | SR |
| 11 | ftextfield | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | felecprdsr | SR | bpchar | 1 |  | √ | '0' | SR |
| 13 | fothernamemrd | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 14 | fsoftprdsf | SF | bpchar | 1 |  | √ | '0' | SF |
| 15 | fothernameprd | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 16 | fbasedatafieldprd | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 17 | fcombofieldmrd | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 18 | fbasedatafieldmrd | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 19 | felecmrdsf | SF | bpchar | 1 |  | √ | '0' | SF |
| 20 | fsoftprdrr | RR | bpchar | 1 |  | √ | '1' | RR |
| 21 | fsoftmrdsf | SF | bpchar | 1 |  | √ | '0' | SF |
| 22 | felecprdir | IR | bpchar | 1 |  | √ | '0' | IR |
| 23 | felecmrdrr | RR | bpchar | 1 |  | √ | '1' | RR |
| 24 | fsoftmrdsr | SR | bpchar | 1 |  | √ | '0' | SR |
| 25 | fsoftmrdus | US | bpchar | 1 |  | √ | '0' | US |
| 26 | felecprdar | AR | bpchar | 1 |  | √ | '0' | AR |
| 27 | felecprdpb | PB | bpchar | 1 |  | √ | '0' | PB |
| 28 | felecprdrr | RR | bpchar | 1 |  | √ | '1' | RR |
| 29 | fsoftprdpb | PB | bpchar | 1 |  | √ | '0' | PB |
| 30 | felecmrdar | AR | bpchar | 1 |  | √ | '0' | AR |
| 31 | felecmrdpb | PB | bpchar | 1 |  | √ | '0' | PB |
| 32 | fsoftmrdir | IR | bpchar | 1 |  | √ | '0' | IR |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_comm_pack_set |  | fid |
| 2 | idx_plm_rm_comm_pack_set_m0 |  | felecprdrr |
