# 研发费用加计扣除底稿-tccit_dev_jjkc_summary

## 研发费用加计扣除底稿-主表 t_tccit_dev_jjkc_sum

- **表名称：** 研发费用加计扣除底稿-主表
- **表名：** t_tccit_dev_jjkc_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: kxssl :本年可享受研发费用加计扣除项目数量: zzhzjz :一、自主研发、合作研发、集中研发（3+7+16+19+23+34） ryrgfy :（一）人员人工费用（4+5+6） zjcsyfhdrygzxj :1.直接从事研发活动人员工资薪金 zjcsyfhdrywxyj :2.直接从事研发活动人员五险一金 wpyfrydlwfy :3.外聘研发人员的劳务费用 zjtrfy :（二）直接投入费用（8+9+10+11+12+13+14+15） yfhdzjxhclfy :1.研发活动直接消耗材料费用 yfhdzjxhrlfy :2.研发活动直接消耗燃料费用 yfhdzjxhdlfy :3.研发活动直接消耗动力费用 mjgyzbkfzzf :4.用于中间试验和产品试制的模具、工艺装备开发及制造费 bgczcypyjybcssdgzf :5.用于不构成固定资产的样品、样机及一般测试手段购置费 yyszcpdjyf :6.用于试制产品的检验费 yqsbwhtzjywxdfy :7.用于研发活动的仪器、设备的运行维护、调整、检验、维修等费用 zrdyfhdyqsbzlf :8.通过经营租赁方式租入的用于研发活动的仪器、设备租赁费 zjfy :（三）折旧费用（17+18） dyqdzjf :1.用于研发活动的仪器的折旧费 dsbdzjf :2.用于研发活动的设备的折旧费 wxzctxfy :（四）无形资产摊销（20+21+22） rjdtxfy :1.用于研发活动的软件的摊销费用 zlqdtxfy :2.用于研发活动的专利权的摊销费用 fzljsdtxfy :3.用于研发活动的非专利技术（包括许可证、专有技术、设计和计算方法等）的摊销费用 xcpsjfy :（五）新产品设计费等（24+25+26+27） xcpsjf :1.新产品设计费 xgygczdf :2.新工艺规程制定费 xyyzdlcsyf :3.新药研制的临床试验费 ktkfjsdxcsyf :4.勘探开发技术的现场试验费 qtxgfy :（六）其他相关费用(29+30+31+32+33) zlffyfzxfbxf :1.技术图书资料费、资料翻译费、专家咨询费、高新科技研发保险费 yfcgfy :2.研发成果的检索、分析、评议、论证、鉴定、评审、评估、验收费用 zscqsqzcdlf :3.知识产权的申请费、注册费、代理费 zgflbcylbcyl :4.职工福利费、补充养老保险费、补充医疗保险费 clfhyf :5.差旅费、会议费 xetzhqtxgfy :（七）经限额调整后的其他相关费用 wtyfhjje :二、委托研发 (36+37+39) wtjnjghgryffsfy :（一）委托境内机构或个人进行研发活动所发生的费用 wtjwjgyffsdfy :（二）委托境外机构进行研发活动发生的费用 yxjjkcdjwjgyffy :其中：允许加计扣除的委托境外机构进行研发活动发生的费用 wtjwgryffsdfy :（三）委托境外个人进行研发活动发生的费用 ndyffyxj :三、年度研发费用小计(2+36×80%+38) bnfyhje :（一）本年费用化金额 bnzbhje :（二）本年资本化金额 bnxcwxzctxe :四、本年形成无形资产摊销额 yqndxcwxzcbntxe :五、以前年度形成无形资产本年摊销额 yxkcdyffy :六、允许扣除的研发费用合计（41+43+44） xkcdtssr :减：特殊收入部分 yxkcyffydjtssr :七、允许扣除的研发费用抵减特殊收入后的金额(45-46) dnxsyfzjxccpdclbf :减：当年销售研发活动直接形成产品（包括组成部分）对应的材料部分 yqxsyfzjxccpdclbf :减：以前年度销售研发活动直接形成产品（包括组成部分）对应材料部分结转金额 bnyxjjkcdyfjf :本年允许加计扣除的研发费用总额（47-48-49） dsjdyxjjkcdyffyje :其中：第四季度允许加计扣除的研发费用金额 qsjdyxjjkcdyffyje :其中：前三季度允许加计扣除的研发费用金额 jjkcbl :八、加计扣除比例（%） bndyffyjjkcze :九、本年研发费用加计扣除总额 dsjdxgfyjjkc :其中：第四季度相关费用加计扣除 qsjdxgfyjjkc :其中：前三季度相关费用加计扣除 xsyfhdxccpyhndkj :十、销售研发活动直接形成产品（包括组成部分）对应材料部分结转以后年度扣减金额 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | foriginalamount | 原始金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原始金额 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fjjkcbljjsff | 加计扣除比例及计算方法 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 9 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 10 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 13 | fdeductiontype | 选择适用优惠政策 | varchar | 50 |  | √ | ' ' | 选择适用优惠政策,枚举: 1 :开发新技术、新产品、新工艺发生的研究开发费用加计扣除 2 :科技型中小企业开发新技术、新产品、新工艺发生的研究开发费用加计扣除 3 :企业为获得创新性、创意性、突破性的产品进行创意设计活动而发生的相关费用加计扣除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dev_jjkc_sum |  | fid |
| 2 | idx_tccit_dev_jjkc_sum |  | forgid,fskssqq,fskssqz |
