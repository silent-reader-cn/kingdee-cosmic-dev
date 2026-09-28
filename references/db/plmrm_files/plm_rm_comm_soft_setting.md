# 公共配置-软件-plm_rm_comm_soft_setting

## 公共配置-软件-主表 t_plm_rm_comm_soft_set

- **表名称：** 公共配置-软件-主表
- **表名：** t_plm_rm_comm_soft_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedatafieldir | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 3 | fcombofieldsr | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 4 | fsr | SR系统需求 | bpchar | 1 |  | √ | '1' | SR系统需求 |
| 5 | fcombofieldus | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 6 | fus | US用户故事 | bpchar | 1 |  | √ | '1' | US用户故事 |
| 7 | fothernamepb | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 8 | fothernamesf | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 9 | fbasedatafieldpb | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 10 | fbasedatafieldsf | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 11 | fcombofieldir | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 12 | fir | IR初始需求 | bpchar | 1 |  | √ | '1' | IR初始需求 |
| 13 | ftextfield | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fcombofieldsf | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 15 | fcombofieldpb | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 16 | fothernameus | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 17 | fothernamesr | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 18 | fbasedatafieldus | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 19 | fbasedatafieldsr | 图标基础资料 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 20 | fsf | SF系统特性 | bpchar | 1 |  | √ | '1' | SF系统特性 |
| 21 | fpb | PB核心问题 | bpchar | 1 |  | √ | '1' | PB核心问题 |
| 22 | fothernameir | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_comm_soft_set_m0 |  | fcombofieldus |
| 2 | pk_plm_rm_comm_soft_set |  | fid |
