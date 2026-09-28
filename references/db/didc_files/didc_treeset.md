# 指标参数设置-didc_treeset

## 指标参数设置-主表 t_didc_treeset

- **表名称：** 指标参数设置-主表
- **表名：** t_didc_treeset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardtoward | 卡片朝向 | varchar | 255 |  | √ | ' ' | 卡片朝向 |
| 3 | ffilterlist | 当前过滤条件 | varchar | 255 |  | √ | ' ' | 当前过滤条件 |
| 4 | fhead | 负责人 | bpchar | 1 |  | √ | ' ' | 负责人 |
| 5 | fuserid | 当前用户id | int8 | 64 |  | √ | 0 | 当前用户id |
| 6 | fyoy | 同比 | bpchar | 1 |  | √ | ' ' | 同比 |
| 7 | ftrend | 变化趋势 | bpchar | 1 |  | √ | ' ' | 变化趋势 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fcardtoward_tag | 卡片朝向_详情 | text | 0 |  |  | null | 卡片朝向_详情 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fscale | 比例大小 | numeric | 23 | 10 | √ | 0 | 比例大小 |
| 12 | fschedule | 进度 | bpchar | 1 |  | √ | ' ' | 进度 |
| 13 | findexname | 关联指标名称 | bpchar | 1 |  | √ | ' ' | 关联指标名称 |
| 14 | ftreeid | 指标树id | int8 | 64 |  | √ | 0 | 指标树id |
| 15 | ftoward | 指标树朝向 | varchar | 50 |  | √ | ' ' | 指标树朝向 |
| 16 | ffilterlist_tag | 当前过滤条件_详情 | text | 0 |  |  | null | 当前过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_treeset |  | fid |
| 2 | idx_didc_treeset |  | fuserid |
