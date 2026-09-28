# 物料优选配置单据-plm_plmsm_mat_prefset

## 物料优选配置单据-主表 t_plmsm_prefer_solution

- **表名称：** 物料优选配置单据-主表
- **表名：** t_plmsm_prefer_solution

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 优选方案名称 | varchar | 255 |  | √ | ' ' | 优选方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdata_tag | 方案内容_详情 | text | 0 |  |  | null | 方案内容_详情 |
| 6 | fschemeid | 过滤方案id | varchar | 255 |  | √ | ' ' | 过滤方案id,枚举: |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fschemename | 过滤方案名称 | varchar | 255 |  | √ | ' ' | 过滤方案名称 |
| 9 | fstatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftype | 取值方式 | bpchar | 1 |  | √ | 'A' | 取值方式,枚举: A :平均值 B :最大值 C :最小值 |
| 12 | fused | 是否执行过 | bpchar | 1 |  | √ | '0' | 是否执行过 |
| 13 | fdata | 方案内容 | varchar | 255 |  | √ | ' ' | 方案内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_prefer_solution |  | fid |
| 2 | idx_t_plmsm_preferred_fchemeid |  | fschemeid |
