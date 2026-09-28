# 入驻审批-pmm_supplieraudit

## 入驻审批-主表 t_mal_supenter

- **表名称：** 入驻审批-主表
- **表名：** t_mal_supenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcentralpurtype | 集采类型 | bpchar | 1 |  | √ | ' ' | 集采类型,枚举: 1 :集采 2 :自由 3 :集采&自由 |
| 3 | fgroupid | 商家分组 | int8 | 64 |  | √ | 0 | 供应商分类 bd_suppliergroup |
| 4 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 5 | fsocietycreditcode | 统一社会信用代码 | varchar | 50 |  | √ | ' ' | 统一社会信用代码 |
| 6 | forgcode | 组织机构代码 | varchar | 50 |  | √ | ' ' | 组织机构代码 |
| 7 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 9 | faccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :入驻 2 :冻结 3 :取消冻结 4 :终止 |
| 11 | fbillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 12 | fbizscope | 企业经营范围 | varchar | 510 |  | √ | ' ' | 企业经营范围 |
| 13 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 14 | fphone | 联系电话 | varchar | 60 |  | √ | ' ' | 联系电话 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 16 | fsuggestion | 审批意见 | varchar | 510 |  | √ | ' ' | 审批意见 |
| 17 | fbank | 开户行名称 | varchar | 100 |  | √ | ' ' | 开户行名称 |
| 18 | freason | 申请入驻理由 | varchar | 510 |  | √ | ' ' | 申请入驻理由 |
| 19 | faccname | 银行账户名称 | varchar | 100 |  | √ | ' ' | 银行账户名称 |
| 20 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 21 | fsupplierid | 申请商家 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :待审批 B :同意 D :不同意 |
| 23 | finvoicetype | 出具发票类型 | bpchar | 1 |  | √ | ' ' | 出具发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 6 :电子普票&专票 7 :纸质普票&专票 |
| 24 | finvoiceid | 出具发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 25 | fpersonid | 申请人 | int8 | 64 |  | √ | 0 | 供应商业务员 pbd_supbizperson |
| 26 | ftxregisterno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 27 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 28 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_supenter_fbizpartnerid |  | fbizpartnerid |
| 2 | idx_mal_supenter_fbillno |  | fbillno |
| 3 | idx_mal_supenter_fbilldate |  | fbilldate |
| 4 | t_mal_supenter_pkey |  | fid |

---

## 入驻商品类别-多选基础资料表 t_mal_supenter_mat

- **表名称：** 入驻商品类别-多选基础资料表
- **表名：** t_mal_supenter_mat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 商品分类 pbd_goodsclass |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_supenter_mat_fid |  | fid,fbasedataid |
| 2 | t_mal_supenter_mat_pkey |  | fpkid |

---

## 资质分录-子表 t_mal_supaptitude

- **表名称：** 资质分录-子表
- **表名：** t_mal_supaptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资质名称 | varchar | 255 |  | √ | ' ' | 资质名称 |
| 3 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 4 | ftype | 资质类型 | bpchar | 1 |  | √ | ' ' | 资质类型,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 5 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fnumber | 资质编号 | varchar | 50 |  | √ | ' ' | 资质编号 |
| 9 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 10 | fcheckdate | 最近年检日期 | timestamp | 0 |  |  | null | 最近年检日期 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fgrade | 资质等级 | varchar | 20 |  | √ | ' ' | 资质等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_supaptitude_fid |  | fid,fseq |
| 2 | t_mal_supaptitude_pkey |  | fentryid |

---

## 入驻审批-分表 t_mal_supenter_a

- **表名称：** 入驻审批-分表
- **表名：** t_mal_supenter_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcfmid | 审批人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_supenter_a_pkey |  | fid |
| 2 | idx_mal_supenter_a_fcreatetime |  | fcreatetime |

---

## 入驻审批-多语言表 t_mal_supenter_l

- **表名称：** 入驻审批-多语言表
- **表名：** t_mal_supenter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | faddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_supenter_l_fid |  | fid,flocaleid |
| 2 | t_mal_supenter_l_pkey |  | fpkid |
