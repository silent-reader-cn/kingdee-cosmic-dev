# 工资薪金项目及跨期扣除项目台账-tccit_salary_intededuct

## 工资薪金项目及跨期扣除项目台账-主表 t_tccit_salary_intededuct

- **表名称：** 工资薪金项目及跨期扣除项目台账-主表
- **表名：** t_tccit_salary_intededuct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpretaxdeductdate | 税前扣除年度 | timestamp | 0 |  |  | null | 税前扣除年度 |
| 7 | fremarks | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcosttype | 费用类型 | varchar | 50 |  | √ | ' ' | 费用类型,枚举: gzxj :工资薪金 zgflf :职工福利费 zgjyjf :职工教育经费 ghjf :工会经费 shbx :社会保险 zfgjj :住房公积金 bcylbx1 :补充医疗保险 bcylbx2 :补充养老保险 qtgzxjxm :其他工资薪金项目 qtkqkcxm :其他跨期扣除项目 dzzgzjf :党组织工作经费 |
| 12 | fprojectname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 13 | fsalarypaytype | 工资薪金支付类型 | varchar | 50 |  | √ | ' ' | 工资薪金支付类型,枚举: 1 :本年计提本年支付工资薪金 2 :本年汇算清缴前支付上年度计提工资 3 :次年汇算清缴前支付本年度已计提工资 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcostcenter | 成本中心 | varchar | 50 |  | √ | ' ' | 成本中心 |
| 16 | faccounttype | 核算类型 | varchar | 50 |  | √ | ' ' | 核算类型,枚举: zmjt :账面计提 sjzf :实际支付 bksqkc :不可税前扣除 wsjzf :未实际支付 |
| 17 | fmoney | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 18 | fdocnumber | 会计凭证编号 | varchar | 50 |  | √ | ' ' | 会计凭证编号 |
| 19 | faccountdate | 会计核算日期 | timestamp | 0 |  |  | null | 会计核算日期 |
| 20 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_salary_intededuct |  | fbillno |
| 2 | pk_tccit_salary_intededuct |  | fid |
