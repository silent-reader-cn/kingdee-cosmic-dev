# 调用统计汇总数据-openapi_statdata

## 调用统计汇总数据-主表 t_openapi_statdata_sum

- **表名称：** 调用统计汇总数据-主表
- **表名：** t_openapi_statdata_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 日期 | int8 | 64 |  | √ | 0 | 日期 |
| 3 | fthirdid | 第三方应用 | int8 | 64 |  | √ | 0 | 第三方应用维护 openapi_3rdapps |
| 4 | ftype | 类型 | int4 | 32 |  | √ | 0 | 类型,枚举: 1 :时明细(24小时) 2 :天明细(90天) 7 :天汇总数据 9 :总汇总数据 |
| 5 | fapiid | API | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 6 | fsuccesscnt | 成功次数 | int8 | 64 |  | √ | 0 | 成功次数 |
| 7 | fcnt | 调用总次数 | int8 | 64 |  | √ | 0 | 调用总次数 |
| 8 | fcost | 调用总耗时 | int8 | 64 |  | √ | 0 | 调用总耗时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftime | ftime,ftype,fapiid,fthirdid |
| 2 | ftype | ftime,ftype,fapiid,fthirdid |
| 3 | fapiid | ftime,ftype,fapiid,fthirdid |
| 4 | fthirdid | ftime,ftype,fapiid,fthirdid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_openapi_stat_sum_typetime |  | ftype,ftime |
| 2 | pk_t_openapi_statdata_sum |  | ftime,ftype,fapiid,fthirdid |
