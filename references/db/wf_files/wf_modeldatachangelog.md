# 模型数据变更记录-wf_modeldatachangelog

## 模型数据变更记录-主表 t_wf_modeldatachangelog

- **表名称：** 模型数据变更记录-主表
- **表名：** t_wf_modeldatachangelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fresourceid | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 5 | fschemeid | 方案ID | int8 | 64 |  | √ | 0 | 方案ID |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fcontent | 原资源内容 | text | 0 |  |  | null | 原资源内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_modeldatalog_procdef |  | fprocdefid |
| 2 | idx_wf_modeldatachangelog |  | fschemeid |
| 3 | pk_t_wf_modeldatachangelog |  | fid |
