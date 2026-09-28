# 创建结算清单后台参数-ism_sysparamdata

## 创建结算清单后台参数-主表 t_ism_sysparamdata

- **表名称：** 创建结算清单后台参数-主表
- **表名：** t_ism_sysparamdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 100 |  | √ | ' ' | 参数值 |
| 3 | fparamkey | 参数标识 | varchar | 50 |  | √ | ' ' | 参数标识,枚举: maxshowrow :创建结算清单最大提示行数（默认值：10000） savemiddledata :当不显示中间结果时是否保存中间结果（默认值：true） maxdatescope :创建结算清单最大日期范围（默认值：31） settlesavemaxsize :保存结算清单的最大批量（默认值：5） midsavemaxsize :保存中间结果的最大批量（默认值：100000） maxpagesettlerow :页面最大一次性处理的结算单据记录数（默认值：200000） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_sysparamdata |  | fid |
| 2 | idx_ism_sysparamdata |  | fparamkey |
