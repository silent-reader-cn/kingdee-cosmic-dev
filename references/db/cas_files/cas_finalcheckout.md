# 出纳期末结账-cas_finalcheckout

## 出纳期末结账-主表 t_cas_finalcheckout

- **表名称：** 出纳期末结账-主表
- **表名：** t_cas_finalcheckout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcheckoutstatus | 结账状态 | varchar | 30 |  | √ | '1' | 结账状态,枚举: 1 :未结账 2 :正在结账 3 :结账成功 4 :结账失败 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftimeconsum | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fperiod | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fbeforeperiod | 上一期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 14 | fcheckoutmsg | 结果 | varchar | 510 |  | √ | ' ' | 结果 |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_finalchk_orgp |  | forgid,fperiod |
| 2 | t_cas_finalcheckout_pkey |  | fid |
