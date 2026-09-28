# 组织进度单元-er_progressunit

## 组织进度单元-主表 t_er_progressunit

- **表名称：** 组织进度单元-主表
- **表名：** t_er_progressunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompleted | 是否完成 | bpchar | 1 |  | √ | ' ' | 是否完成 |
| 3 | fbaseaccorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | finitialgroupid | 初始化任务项分类 | int8 | 64 |  | √ | 0 | [初始化任务项分类维护（废弃） er_initialgroup](../em_files/er_initialgroup.md) |
| 5 | finitialconfigid | 初始化配置项 | int8 | 64 |  | √ | 0 | [初始化任务项（废弃） er_initialconfig](../em_files/er_initialconfig.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_progressunit |  | fcompleted,finitialconfigid,finitialgroupid,fbaseaccorgid |
| 2 | pk_t_er_progressunit |  | fid |
