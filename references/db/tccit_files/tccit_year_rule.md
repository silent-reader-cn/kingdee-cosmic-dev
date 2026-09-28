# 年报取数规则-tccit_year_rule

## 取数规则-子表 t_tccit_item_fetchentry

- **表名称：** 取数规则-子表
- **表名：** t_tccit_item_fetchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | fexratejson | 汇率转换 | varchar | 255 |  | √ | ' ' | 汇率转换 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 5 | fadvancedconfjson | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 9 | fvatrate | 增值税税率 | numeric | 23 | 10 | √ | 0 | 增值税税率 |
| 10 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 11 | fiscustomtable | fiscustomtable | bpchar | 1 |  | √ | ' ' |  |
| 12 | fadvancedconf | 取数逻辑 | text | 0 |  |  | null | 取数逻辑 |
| 13 | fprojecttype | 项目类型 | varchar | 30 |  | √ | ' ' | 项目类型,枚举: zzje :账载金额取数配置 sjje :实际金额取数配置 bksqlzje :不可税前列支金额取数配置 stxs_sr :视同销售收入取数配置 stxs_cb :视同销售成本取数配置 swkjje :税务口径金额取数配置 byxkcdgxfje :不允许扣除的广宣费金额取数配置 gjzqtglfdgxfje :归集至其他关联方的广宣费金额取数配置 qtglfgjzbqydgxfje :其他关联方归集至本企业的广宣费金额取数配置 bnssje :本年税收金额取数配置 ljssje :累计税收金额取数配置 bnzzje :本年账载金额取数配置 ljzzje :累计账载金额取数配置 ssje :税收金额取数配置 cqgqtz :按权益法核算长期股权投资对初始投资成本调整确认收益取数配置 jrzccstz :交易性金融资产初始投资调整取数配置 zmjt :账面计提的非金融机构借款利息取数规则配置 sjzffjr :实际支付的非金融机构借款利息取数规则配置 cgjrqydk :超过金融企业同期同类贷款利率的利息支出取数规则配置 tzwdw :投资未到位而发生的利息支出取数规则配置 zbrhbkkc :资本弱化不可扣除的利息支出取数规则配置 qtbkkc :其他不可扣除的利息支出取数规则配置 zzjeqs :账载金额取数规则配置 byxkcje :不允许扣除的金额取数规则配置 xekcjs :限额扣除基数取数规则配置 bfsr :保费收入取数规则配置 tbje :退保金额取数规则配置 nstzje :纳税调整金额取数规则配置 cjqrcz :会计确认的处置收入取数规则配置 swqrcz :税务确认的处置收入取数规则配置 tzzczmjz :投资资产账面价值取数规则配置 tzzcjsjc :投资资产计税基础取数规则配置 zczzyz :会计资产原值 bnzjtxzzje :本年会计折旧摊销 ljzjtxzzje :累计会计折旧摊销 zcjsjc :计税基础 bnsszjtxze :本年税务折旧摊销 ljsszjtxje :累计税务折旧摊销 bnjszjtxje :本年加速折旧摊销金额 bnxsjszc :享受加速折旧政策的资产按税收一般规定计算的折旧、摊销额 ljjszjtxje :累计加速折旧摊销金额 profit :取数规则配置 assetsloss :资产损失直接计入本年损益金额 assetsoriginal :资产原值 assetssumdepreciate :资产累计税务折旧摊销 assetsabnormalincome :非正常损失进项转出 assetsdisposalincome :资产处置收入 assetsdamagesincome :资产赔偿收入 assetsreserveverify :资产损失准备金核销金额 sjfsje :实际发生金额取数配置 sjzcje :实际支出金额取数规则配置 wqdhgpj :未取得合规票据金额取数规则配置 ybswclzzje :一般税务处理的账载金额 ybswclssje :一般税务处理的税收金额 tsswclzzje :特殊税务处理的账载金额 tsswclssje :特殊税务处理的税收金额 snmdkzcye :上年末贷款资产余额 bnmdkzcye :本年末贷款资产余额 snmdksszbjye :上年末贷款损失准备金余额 bnmdksszbjye :本年末贷款损失准备金余额 snmzytqdksszbjddkzcye :上年末准予提取贷款损失准备金的贷款资产余额 bnmzytqdksszbjddkzcye :本年末准予提取贷款损失准备金的贷款资产余额 zjcsyfhdrygzxj :直接从事研发活动人员工资薪金 zjcsyfhdrywxyj :直接从事研发活动人员五险一金 wpyfrydlwfy :外聘研发人员的劳务费用 yfhdzjxhclfy :研发活动直接消耗材料费用 yfhdzjxhrlfy :研发活动直接消耗燃料费用 yfhdzjxhdlfy :研发活动直接消耗动力费用 mjgyzbkfzzf :用于中间试验和产品试制的模具、工艺装备开发及制造费 bgczcypyjybcssdgzf :用于不构成固定资产的样品、样机及一般测试手段购置费 yyszcpdjyf :用于试制产品的检验费 yqsbwhtzjywxdfy :用于研发活动的仪器、设备的运行维护、调整、检验、维修等费用 zrdyfhdyqsbzlf :通过经营租赁方式租入的用于研发活动的仪器、设备租赁费 dyqdzjf :用于研发活动的仪器的折旧费 dsbdzjf :用于研发活动的设备的折旧费 rjdtxfy :用于研发活动的软件的摊销费用 zlqdtxfy :用于研发活动的专利权的摊销费用 fzljsdtxfy :用于研发活动的非专利技术（包含许可证、专有技术、设计和计算方法等）的摊销费用 xcpsjf :新产品设计费 xgygczdf :新工艺规程制定费 xyyzdlcsyf :新药研制的临床试验费 ktkfjsdxcsyf :勘探开发技术的现场试验费 zlffyfzxfbxf :技术图书资料费、资料翻译费、专家咨询费、高新科技研发保险费 yfcgfy :研发成果的检索、分析、评议、论证、鉴定、评审、评估、验收费用 zscqsqzcdlf :知识产权的申请费、注册费、代理费 zgflbcylbcyl :职工福利费、补充养老保险费、补充医疗保险费 clfhyf :差旅费、会议费 xetzhqtxgfy :经限额调整后其他相关费用 wtjnjghgryffsfy :委托境内机构或个人进行研发活动所发生的费用 wtjwjgyffsdfy :委托境外机构进行研发活动发生的费用 yxjjkcdjwjgyffy :其中：允许加计扣除的委托境外机构进行研发活动发生的费用 wtjwgryffsdfy :委托境外个人进行研发活动发生的费用 bnfyhje :本年费用化金额 bnzbhje :本年资本化金额 bnxcwxzctxe :本年形成无形资产摊销额 yqndxcwxzcbntxe :以前年度形成无形资产本年摊销额 xkcdtssr :需扣除的特殊收入 dnxsyfzjxccpdclbf :当年销售研发活动直接形成产品对应的材料部分 bncyxhhctqy :本年从有限合伙创投企业应分得的应纳税所得额 bnxzdkdktze :本年新增的符合条件的股权投资额 bnyxdmdtze :本年允许抵免的投资额 xswsgcpsr :销售未完工产品的收入 xswsgcpzwgcpqrxssr :销售未完工产品转完工产品确认的销售收入 sjfsdyysjjfjtdzzs :实际发生的营业税金及附加、土地增值税 zhsjfsdyysjjfjtdzzs :转回实际发生的营业税金及附加、土地增值税 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 16 | fdatadirection | 取数方向 | varchar | 30 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | fdatatype | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_item_fetchentry_pkey |  | fentryid |
| 2 | idx_tccit_item_fetchentry |  | fid |

---

## 年报取数规则-主表 t_tccit_year_rule

- **表名称：** 年报取数规则-主表
- **表名：** t_tccit_year_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fspap | 自产/外购 | varchar | 50 |  | √ | ' ' | 自产/外购,枚举: self :自产 out :外购 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fruletype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 7 | fbusinessfeature | 业务特性 | varchar | 30 |  | √ | ' ' | 业务特性,枚举: 1 :以发票口径为应税销售额 2 :以会计口径为应税销售额 4 :以发票和会计口径孰大原则确认应税销售额 |
| 8 | fitemid | 取数项目选择 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcosttype | 费用归集 | varchar | 30 |  | √ | ' ' | 费用归集,枚举: manage :管理费用 sale :销售费用 financing :财务费用 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fitemtype | 取数项目类型 | varchar | 50 |  | √ | ' ' | 取数项目类型,枚举: tpo_discount_tree :优惠项目（树） tpo_yearitems_tree :项目取数（树） |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: income :收入成本 period :期间费用 ajust :扣除调整 dsale :视同销售 zcajust :资产调整 srajust :收入调整 tssx :特殊事项调整 other :其他 ssyh :税收优惠 |
| 16 | fvatrate | fvatrate | numeric | 23 | 10 | √ | 0 |  |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_year_rule_pkey |  | fid |
| 2 | idx_tccit_year_rule |  | fnumber |

---

## 年报取数规则-多语言表 t_tccit_year_rule_l

- **表名称：** 年报取数规则-多语言表
- **表名：** t_tccit_year_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_year_rule_l_0 |  | fid,flocaleid |
| 2 | t_tccit_year_rule_l_pkey |  | fpkid |
