# 停止同步单据配置文本表-cal_stopsyncset_sup

## 停止同步单据配置文本表-主表 t_cal_stopsyncset_sup

- **表名称：** 停止同步单据配置文本表-主表
- **表名：** t_cal_stopsyncset_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparentid | 启动停止同步单据设置id | int8 | 64 |  | √ | 0 | 启动停止同步单据设置id |
| 2 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_stopsyncset_sup |  | fparentid,fbillid |
| 2 | pk_cal_stopsyncset_sup |  | fentryid |
