# 共享中心工作日历初始化-ssc_workcalendar_init

## 共享中心工作日历初始化-主表 t_tk_workcalendar_init

- **表名称：** 共享中心工作日历初始化-主表
- **表名：** t_tk_workcalendar_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finituser | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finitcontent | 初始化内容 | varchar | 255 |  | √ | ' ' | 初始化内容 |
| 4 | finitcontent_tag | 初始化内容_详情 | text | 0 |  |  | null | 初始化内容_详情 |
| 5 | fssc | 初始化共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finitdate | 初始化日期 | timestamp | 0 |  |  | null | 初始化日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_workcalendar_init |  | fid |
| 2 | idx_ssc_workcalendarinit_union |  | fssc |
