# 税局申报预填单据-tcvat_declare_sjyt

## 税局申报预填单据-主表 t_tcvat_declare_sjyt

- **表名称：** 税局申报预填单据-主表
- **表名：** t_tcvat_declare_sjyt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fkjskzzszyfpxxynse | 开具增值税专用发票销项应纳税额 | numeric | 23 | 10 | √ | 0 | 开具增值税专用发票销项应纳税额 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fkjqtfpxse | 开具其他发票销售额 | numeric | 23 | 10 | √ | 0 | 开具其他发票销售额 |
| 8 | fkjskzzszyfpxse | 开具增值税专用发票销售额 | numeric | 23 | 10 | √ | 0 | 开具增值税专用发票销售额 |
| 9 | fkjqtfpxxynse | 开具其他发票销项应纳税额 | numeric | 23 | 10 | √ | 0 | 开具其他发票销项应纳税额 |
| 10 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 11 | ffs | 份数 | numeric | 23 | 10 | √ | 0 | 份数 |
| 12 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fse | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | fsbbhmc | 申报表行名称 | varchar | 50 |  | √ | ' ' | 申报表行名称,枚举: tcvat_ybnsr_fb1#1 :13%税率的货物及加工修理修配劳务 tcvat_ybnsr_fb1#2 :13%税率的服务、不动产和无形资产 tcvat_ybnsr_fb1#23 :9%税率的货物及加工修理修配劳务 tcvat_ybnsr_fb1#4 :9%税率的服务、不动产和无形资产 tcvat_ybnsr_fb1#5 :6%税率 tcvat_ybnsr_fb1#8 :6%征收率 tcvat_ybnsr_fb1#9 :5%征收率的货物及加工修理修配劳务 tcvat_ybnsr_fb1#22 :5%征收率的服务、不动产和无形资产 tcvat_ybnsr_fb1#10 :4%征收率 tcvat_ybnsr_fb1#11 :3%征收率的货物及加工修理修配劳务 tcvat_ybnsr_fb1#12 :3%征收率的服务、不动产和无形资产 tcvat_ybnsr_fb1#13 :预征率_13a tcvat_ybnsr_fb1#20 :预征率_13b tcvat_ybnsr_fb1#21 :预征率_13c tcvat_ybnsr_fb1#16 :免抵退税_货物及加工修理修配劳务 tcvat_ybnsr_fb1#17 :免抵退税_服务、不动产和无形资产 tcvat_ybnsr_fb1#18 :免税_货物及加工修理修配劳务 tcvat_ybnsr_fb1#19 :免税_服务、不动产和无形资产 tcvat_ybnsr_fb2#2 :第2栏_其中：本期认证相符且本期申报抵扣 tcvat_ybnsr_fb2#3 :第3栏_前期认证相符且本期申报抵扣 tcvat_ybnsr_fb2#5 :第5栏_其中：海关进口增值税专用缴款书 tcvat_ybnsr_fb2#6 :第6栏_农产品收购发票或者销售发票 tcvat_ybnsr_fb2#7 :第7栏_代扣代缴税收缴款凭证 tcvat_ybnsr_fb2#37 :第8a栏_ 加计扣除农产品进项税额 tcvat_ybnsr_fb2#8 :第8b栏_其他 tcvat_ybnsr_fb2#9 :第9栏_（三） 本期用于购建不动产的扣税凭证 tcvat_ybnsr_fb2#10 :第10栏_（四）本期用于抵扣的旅客运输服务扣税凭证 tcvat_ybnsr_fb2#11 :第11栏_（五）外贸企业进项税额抵扣证明 tcvat_ybnsr_fb2#14 :第14栏_其中：免税项目用 tcvat_ybnsr_fb2#15 :第15栏_集体福利、个人消费 tcvat_ybnsr_fb2#16 :第16栏_非正常损失 tcvat_ybnsr_fb2#17 :第17栏_简易计税方法征税项目用 tcvat_ybnsr_fb2#18 :第18栏_免抵退税办法不得抵扣的进项税额 tcvat_ybnsr_fb2#19 :第19栏_纳税检查调减进项税额 tcvat_ybnsr_fb2#20 :第20栏_ 红字专用发票信息表注明的进项税额 tcvat_ybnsr_fb2#21 :第21栏_上期留抵税额抵减欠税 tcvat_ybnsr_fb2#22 :第22栏_上期留抵税额退税 tcvat_ybnsr_fb2#23a :第23a栏_异常凭证转出进项税额 tcvat_ybnsr_fb2#23 :第23b栏_其他应作进项税额转出的情形 tcvat_ybnsr_fb2#25 :第25栏_期初已认证相符但未申报抵扣 tcvat_ybnsr_fb2#26 :第26栏_本期认证相符且本期未申报抵扣 tcvat_ybnsr_fb2#27 :第27栏_ 期末已认证相符但未申报抵扣 tcvat_ybnsr_fb2#28 :第28栏_其中：按照税法规定不允许抵扣 tcvat_ybnsr_fb2#30 :第30栏_其中：海关进口增值税专用缴款书 tcvat_ybnsr_fb2#31 :第31栏_农产品收购发票或者销售发票 tcvat_ybnsr_fb2#32 :第32栏_代扣代缴税收缴款凭证 tcvat_ybnsr_fb2#33 :第33栏_其他 tcvat_sb_fjsf#1 :增值税免抵税额 tcvat_ybnsr_zb#1 :免、抵、退应退税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_declare_sjyt |  | fid |
| 2 | pk_sjyt_forgid_idx |  | forgid,fskssqz |
