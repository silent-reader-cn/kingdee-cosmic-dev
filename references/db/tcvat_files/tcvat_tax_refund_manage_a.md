# 留抵退税管理台账-tcvat_tax_refund_manage_a

## 留抵退税管理台账-主表 t_tcvat_tax_refund_mag_a

- **表名称：** 留抵退税管理台账-主表
- **表名：** t_tcvat_tax_refund_mag_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsqldsets | 上期留抵税额退税 | numeric | 23 | 10 | √ | 0 | 上期留抵税额退税 |
| 3 | fbndzzsysxsehj | 本年度增值税应税销售额合计 | numeric | 23 | 10 | √ | 0 | 本年度增值税应税销售额合计 |
| 4 | fbqksqthclldse | 本期可申请退还存量留抵税额x | numeric | 23 | 10 | √ | 0 | 本期可申请退还存量留抵税额x |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fzzssbbbh | 增值税申报表编号 | varchar | 50 |  | √ | ' ' | 增值税申报表编号 |
| 7 | fsqmdsedjqs | 上期留抵税额抵减欠税 | numeric | 23 | 10 | √ | 0 | 上期留抵税额抵减欠税 |
| 8 | finputrate | 进项构成比例(%) | numeric | 23 | 10 | √ | 0 | 进项构成比例(%) |
| 9 | fzzszyfpse | 累计已抵扣增值税专用发票税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣增值税专用发票税额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnsxydj | 纳税信用等级 | varchar | 50 |  | √ | ' ' | 纳税信用等级 |
| 12 | fbqsqthclldtse | 本期申请退还存量留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期申请退还存量留抵退税额 |
| 13 | fbqsbdkjxsehj | 本期申报抵扣进项税额合计 | numeric | 23 | 10 | √ | 0 | 本期申报抵扣进项税额合计 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fhgzyjksse | 累计已抵扣海关专用缴款书税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣海关专用缴款书税额 |
| 16 | fsummonth | 本年度合计月数 | int8 | 64 |  | √ | 0 | 本年度合计月数 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fbqjjskwspzse | 本期解缴税款完税凭证税额 | numeric | 23 | 10 | √ | 0 | 本期解缴税款完税凭证税额 |
| 19 | fqygm | 企业规模 | varchar | 50 |  | √ | ' ' | 企业规模,枚举: dxqy :大型企业 zxqy :中型企业 xxqy :小型企业 wxqy :微型企业 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fskssqq | 所属税期期起 | timestamp | 0 |  |  | null | 所属税期期起 |
| 22 | ftsqylx | 退税企业类型 | varchar | 50 |  | √ | ' ' | 退税企业类型,枚举: xxqy :小型企业 wxqy :微型企业 nlmyy :农、林、牧、渔业 zzy :制造业 kxyjhjsfwy :科学研究和技术服务业 dlrlrqjsschgyy :电力、热力、燃气及水生产和供应业 rjhxxjsfwy :软件和信息技术服务业 stbhhhjzly :生态保护和环境治理业 jtyscchyzy :交通运输、仓储和邮政业 pfhlsy :批发和零售业 zshcyy :住宿和餐饮业 jmfwxlhqtfwy :居民服务、修理和其他服务业 jy :教育 wshshgz :卫生和社会工作 whtyhyly :文化、体育和娱乐业 ybqy :一般企业 |
| 23 | fbqmdtytse | 本期免抵退应退税额 | numeric | 23 | 10 | √ | 0 | 本期免抵退应退税额 |
| 24 | fljdkjjkwspzse | 累计已抵扣解缴税款完税凭证税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣解缴税款完税凭证税额 |
| 25 | fbqksqthzlldse | 本期可申请退还增量留抵税额y | numeric | 23 | 10 | √ | 0 | 本期可申请退还增量留抵税额y |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fdqxzkyytcdldtse | 当期新增可用于扣除的留抵退税额 | numeric | 23 | 10 | √ | 0 | 当期新增可用于扣除的留抵退税额 |
| 28 | fzlldtserq | 增量留抵退税额日期 | varchar | 200 |  | √ | ' ' | 增量留抵退税额日期 |
| 29 | fsqthxm | 申请退还项目 | varchar | 50 |  | √ | ' ' | 申请退还项目,枚举: clldse :存量留抵税额 zlldse :增量留抵税额 clldsezlldse :存量留抵税额、增量留抵税额 |
| 30 | famount | 本期期末留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期期末留抵退税额 |
| 31 | fbqsqthzlldtse | 本期申请退还增量留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期申请退还增量留抵退税额 |
| 32 | fbqksqthldtse | 本期可申请退还留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期可申请退还留抵退税额 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fskssqz | 所属税期期止 | timestamp | 0 |  |  | null | 所属税期期止 |
| 35 | fclldse | 存量留抵税额 | numeric | 23 | 10 | √ | 0 | 存量留抵税额 |
| 36 | ftsbljd | 退税办理进度 | varchar | 50 |  | √ | ' ' | 退税办理进度,枚举: wsq :未申请 ysq :已申请 zyts :准予退税 yts :已退税 null :-- |
| 37 | fljdkjxse | 累计已申报抵扣进项税额合计 | numeric | 23 | 10 | √ | 0 | 累计已申报抵扣进项税额合计 |
| 38 | fbqrzxfdzpse | 本期认证相符的专票税额 | numeric | 23 | 10 | √ | 0 | 本期认证相符的专票税额 |
| 39 | fldtsbqkce | 留抵退税本期扣除额 | numeric | 23 | 10 | √ | 0 | 留抵退税本期扣除额 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fsshydl | 所属行业大类 | varchar | 200 |  | √ | ' ' | 所属行业大类 |
| 42 | fldtssqbbm | 留抵退税申请表编号 | varchar | 50 |  | √ | ' ' | 留抵退税申请表编号 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fktsbl | 可退税比例(%) | numeric | 23 | 10 | √ | 0 | 可退税比例(%) |
| 45 | fsqjckyykcdldtse | 上期结存可用于扣除的留抵退税额 | numeric | 23 | 10 | √ | 0 | 上期结存可用于扣除的留抵退税额 |
| 46 | fsndzzsysxsehj | 上年度增值税应税销售额合计 | numeric | 23 | 10 | √ | 0 | 上年度增值税应税销售额合计 |
| 47 | fjzxqkyykcdldtse | 结转下期可用于扣除的留抵退税额 | numeric | 23 | 10 | √ | 0 | 结转下期可用于扣除的留抵退税额 |
| 48 | fzytssj | 准予退税时间 | varchar | 50 |  | √ | ' ' | 准予退税时间 |
| 49 | fsnmzcze | 上年末资产总额 | numeric | 23 | 10 | √ | 0 | 上年末资产总额 |
| 50 | fbqdkhgzyjksse | 本期抵扣海关专用缴款书税额 | numeric | 23 | 10 | √ | 0 | 本期抵扣海关专用缴款书税额 |
| 51 | fstartqmldse | 2019年3月期末留抵税额 | numeric | 23 | 10 | √ | 0 | 2019年3月期末留抵税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_tax_refund_mag_a |  | fid |
| 2 | idx_tcvat_tax_refund_fbillno |  | fbillno |
