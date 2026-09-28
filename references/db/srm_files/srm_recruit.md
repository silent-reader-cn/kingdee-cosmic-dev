# 招募发布-srm_recruit

## 品类分类-子表 t_pur_recruitentry

- **表名称：** 品类分类-子表
- **表名：** t_pur_recruitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 招募品类 | varchar | 255 |  | √ | ' ' | 招募品类 |
| 3 | fyearamount | 年计划采购额(万) | numeric | 19 | 6 | √ | 0.000000 | 年计划采购额(万) |
| 4 | ftrade | 所属行业 | varchar | 255 |  | √ | ' ' | 所属行业 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdescription | 需求描述 | varchar | 255 |  | √ | ' ' | 需求描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_recruitentry_pkey |  | fentryid |
| 2 | idx_pur_recruitentry_fid_fseq |  | fid,fseq |

---

## 招募发布-多语言表 t_pur_recruit_l

- **表名称：** 招募发布-多语言表
- **表名：** t_pur_recruit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_recruit_l_fid |  | fid,flocaleid |
| 2 | t_pur_recruit_l_pkey |  | fpkid |

---

## 招募发布-主表 t_pur_recruit

- **表名称：** 招募发布-主表
- **表名：** t_pur_recruit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 招募组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizstatus | 项目状态 | bpchar | 1 |  | √ | ' ' | 项目状态,枚举: A :待发布 B :招募中 C :已完成 Z :已终止 |
| 4 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 5 | ftitle | 招募标题 | varchar | 255 |  | √ | ' ' | 招募标题 |
| 6 | fenddate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 7 | fbiztype | 招募类型 | bpchar | 1 |  | √ | ' ' | 招募类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 8 | fbizmodel | 经营模式 | varchar | 50 |  | √ | ' ' | 经营模式,枚举: 1 :生产加工 2 :经销批发 3 :商业服务 4 :招商代理 |
| 9 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 9 :不需要发票 |
| 10 | fcertificate | 证照要求 | varchar | 50 |  | √ | ' ' | 证照要求,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 11 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 12 | fbillno | 招募单号 | varchar | 80 |  | √ | ' ' | 招募单号 |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 18 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 pur_paycond](../basedata_files/pur_paycond.md) |
| 19 | fregcapital | 注册资金(万) | numeric | 19 | 6 | √ | 0.000000 | 注册资金(万) |
| 20 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 21 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 22 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 23 | fbizaddr | 经营地址 | varchar | 255 |  | √ | ' ' | 经营地址 |
| 24 | fcontent_tag | 招募说明_详情 | text | 0 |  |  | null | 招募说明_详情 |
| 25 | fpersonid | 联系人 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 26 | fcontent | 招募说明 | text | 0 |  |  | null | 招募说明 |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_recruit_fbillno |  | fbillno |
| 2 | t_pur_recruit_pkey |  | fid |
| 3 | idx_pur_recruit_fbilldate |  | fbilldate |

---

## 招募发布-分表 t_pur_recruit_a

- **表名称：** 招募发布-分表
- **表名：** t_pur_recruit_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpushnotice | 发布公告否 | int8 | 64 |  | √ | 0 | 发布公告否,枚举: 0 :未发布 1 :已发布 |
| 6 | fcfmopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fpush1688 | 发布1688否 | int8 | 64 |  | √ | 0 | 发布1688否,枚举: 0 :未发布 1 :已发布 |
| 9 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_recruit_a_fcreatetime |  | fcreatetime |
| 2 | t_pur_recruit_a_pkey |  | fid |
