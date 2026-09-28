# 基础设置-plm_rm_rr_base_set

## 基础设置-主表 t_plm_rm_rr_base_set

- **表名称：** 基础设置-主表
- **表名：** t_plm_rm_rr_base_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fothernamerr | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 3 | fcombofieldrr | 图标 | varchar | 50 |  | √ | ' ' | 图标,枚举: |
| 4 | frrdoc | 在线需求文档 | bpchar | 1 |  | √ | '0' | 在线需求文档 |
| 5 | fbasedatafieldrr | 图标基础资料 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 6 | ftextfield | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_rr_base_set_m0 |  | fcombofieldrr |
| 2 | pk_plm_rm_rr_base_set |  | fid |
