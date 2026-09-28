# 勾选台账-rim_select_account

## 勾选台账-主表 t_rim_select_account

- **表名称：** 勾选台账-主表
- **表名：** t_rim_select_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpre_authenticate_flag | 操作前认证状态 | varchar | 2 |  | √ | ' ' | 操作前认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 3 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fbatch_no | 批次号 | varchar | 36 |  | √ | ' ' | 批次号 |
| 7 | fmanage_status | 管理状态 | varchar | 2 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 8 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 9 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 10 | fselect_opera_type | 操作方式 | varchar | 2 |  | √ | ' ' | 操作方式,枚举: 1 :手工勾选 2 :自动勾选 3 :外部接口 |
| 11 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 12 | fhandle_status | 处理状态 | varchar | 2 |  | √ | ' ' | 处理状态,枚举: 0 :未处理 3 :处理中 1 :成功 2 :失败 |
| 13 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fcreater | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fselect_result | 勾选返回状态 | varchar | 2 |  | √ | ' ' | 勾选返回状态,枚举: 1 :成功 2 :无此票 3 :该票异常无法认证 4 :该票已认证过 5 :该票已经逾期无法认证 7 :申请认证月份已过期 8 :税局勾选认证不稳定，请稍后再试 10 :该票超出可操作开票日期范围上限 11 :该票已作废 12 :该票已红冲 13 :未申报，属期尚未切换 15 :失控发票 16 :红字发票不能认证 17 :该发票类型不符合退税认证条件 18 :有效税额不合法 19 :已勾选 20 :当期已锁定勾选 21 :管理状态异常 31 :数据校验异常 32 :认证期限校验异常 23 :发票当前未勾选 24 :勾选属期非当前属期,不能取消 25 :当前勾选用途非抵扣勾选 26 :当前勾选用途非不抵扣勾选 33 :当前税号没有申请软证书 34 :勾选服务异常 35 :勾选中 36 :全电平台登录失败 |
| 16 | fnot_deductible_type | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 17 | forg_id | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fdeduction_purpose | 操作类型 | varchar | 2 |  | √ | ' ' | 操作类型,枚举: 1 :抵扣勾选 -1 :取消抵扣勾选 4 :不抵扣勾选 -4 :取消不抵扣勾选 5 :预勾选 -5 :取消预勾选 6 :旅客运输抵扣 -6 :取消旅客运输抵扣 |
| 19 | ftotal_tax_amount | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 20 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 21 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 22 | fselect_status | 是否勾选 | varchar | 2 |  | √ | ' ' | 是否勾选,枚举: 0 :否 1 :是 |
| 23 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 24 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 25 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_select_account |  | finvoice_code,finvoice_no |
| 2 | idx_rim_serialno |  | fserial_no |
| 3 | idx_rim_select_account_status |  | fhandle_status |
| 4 | pk_rim_select_account |  | fid |
