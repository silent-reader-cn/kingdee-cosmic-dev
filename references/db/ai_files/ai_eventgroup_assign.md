# 事件分组分配关系-ai_eventgroup_assign

## 事件分组分配关系-主表 t_ai_eventgroup_assign

- **表名称：** 事件分组分配关系-主表
- **表名：** t_ai_eventgroup_assign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | feventgroupid | 事件分组 | int8 | 64 |  | √ | 0 | [异构数据对接模型分组 ai_eventgroup](../ai_files/ai_eventgroup.md) |
| 4 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_eventgroup_assign |  | feventgroupid,fappid,fuseorgid |
| 2 | pk_t_ai_eventgroup_assign |  | fid |
