# 开票申请单回填发票-sim_bill_add_invoice

## 开票申请单回填发票-主表 t_sim_bill_add_invoice

- **表名称：** 开票申请单回填发票-主表
- **表名：** t_sim_bill_add_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fserialno | 回填批次号 | varchar | 50 |  | √ | ' ' | 回填批次号 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | foriginalbillid | 原始单据主键 | int8 | 64 |  | √ | 0 | 原始单据主键 |
| 8 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fiscancel | 是否取消回填 | varchar | 10 |  | √ | '0' | 是否取消回填,枚举: 0 :没有取消 1 :取消回填 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftotaltax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: |
| 15 | fissuetime | 开票时间 | timestamp | 0 |  |  | null | 开票时间 |
| 16 | finvoiceamount | 发票金额（不含税） | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额（不含税） |
| 17 | finvoiceid | 发票id | varchar | 50 |  | √ | ' ' | 发票id |
| 18 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 19 | fbilldetailid | 单据明细ID | varchar | 50 |  |  | ' ' | 单据明细ID |
| 20 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 21 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fwritebacklable | 是否回写标志 | varchar | 10 |  | √ | '0' | 是否回写标志,枚举: 0 :未回写 1 :回写成功 2 :取消回填回写 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_bill_add_invoice |  | fid |
| 2 | idx_sim_bill_add_invoice |  | foriginalbillid |
