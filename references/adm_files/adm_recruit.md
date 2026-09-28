# 招募查询-adm_recruit

## 招募查询-多语言表 t_pur_recruit_l

- **表名称：** 招募查询-多语言表
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

## 招募查询-主表 t_pur_recruit

- **表名称：** 招募查询-主表
- **表名：** t_pur_recruit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 招募方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbizstatus | 项目状态 | bpchar | 1 |  | √ | ' ' | 项目状态,枚举: A :待发布 B :招募中 C :已完成 Z :已终止 |
| 4 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 5 | ftitle | 招募标题 | varchar | 255 |  | √ | ' ' | 招募标题 |
| 6 | fenddate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 7 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 8 | fbizmodel | fbizmodel | varchar | 50 |  | √ | ' ' |  |
| 9 | finvtype | finvtype | bpchar | 1 |  | √ | ' ' |  |
| 10 | fcertificate | fcertificate | varchar | 50 |  | √ | ' ' |  |
| 11 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 12 | fbillno | 招募单号 | varchar | 80 |  | √ | ' ' | 招募单号 |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 18 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 19 | fregcapital | fregcapital | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 21 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 22 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 23 | fbizaddr | fbizaddr | varchar | 255 |  | √ | ' ' |  |
| 24 | fcontent_tag | 招募说明_详情 | text | 0 |  |  | null | 招募说明_详情 |
| 25 | fpersonid | 招募人员 | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
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

## 招募查询-分表 t_pur_recruit_a

- **表名称：** 招募查询-分表
- **表名：** t_pur_recruit_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpushnotice | fpushnotice | int8 | 64 |  | √ | 0 |  |
| 6 | fcfmopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fpush1688 | fpush1688 | int8 | 64 |  | √ | 0 |  |
| 9 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_recruit_a_fcreatetime |  | fcreatetime |
| 2 | t_pur_recruit_a_pkey |  | fid |
