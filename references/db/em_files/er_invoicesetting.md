# 开票设置-er_invoicesetting

## 开票设置-多语言表 t_er_invoicesetting_l

- **表名称：** 开票设置-多语言表
- **表名：** t_er_invoicesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 开票名称 | varchar | 100 |  | √ | ' ' | 开票名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_invoicesetting_l_pkey |  | fpkid |
| 2 | idx_er_invsetting_l_lcid |  | flocaleid,fid |

---

## 开票设置-主表 t_er_invoicesetting

- **表名称：** 开票设置-主表
- **表名：** t_er_invoicesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fisp | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :未审核 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicesetting_isp |  | fisp |
| 2 | t_er_invoicesetting_pkey |  | fid |

---

## 单据体-子表 t_er_invoicesettingentry

- **表名称：** 单据体-子表
- **表名：** t_er_invoicesettingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fserviceitem | 服务项目 | varchar | 10 |  | √ | ' ' | 服务项目,枚举: INSURANCE :保险费 SERVICE :服务费 TICKET :票价 ITINERARY :机票行程单 TICKREFUND :行程单-退票费 |
| 3 | foperationtype | 服务类型 | varchar | 10 |  | √ | ' ' | 服务类型,枚举: 2 :国内机票 1 :国内酒店 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 8 :用餐预订 |
| 4 | finvoicetype | 开票类型 | varchar | 10 |  | √ | ' ' | 开票类型,枚举: 0 :增值税普通发票（纸质） 1 :增值税专用发票（纸质） 2 :增值税普通发票（电子） 3 :机票行程单 4 :火车票 5 :定额发票 6 :增值税专用发票（电子） |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 7 | fbrief | 发票摘要 | varchar | 10 |  | √ | ' ' | 发票摘要,枚举: 0 :机票住宿费 1 :机票费 2 :退票费 3 :代理服务费 4 :机票签证费 5 :机票用车费 6 :商旅服务费 9 :代订住宿费 10 :保险费 7 :火车票 11 :*运输服务*客运服务费 12 :经济代理*代订餐费 13 :经济代理*服务费 16 :代订用车费 |
| 8 | fdeductrate | 可抵扣税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税率(%) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_invsetent_id_seq |  | fid,fseq |
| 2 | t_er_invoicesettingentry_pkey |  | fentryid |
