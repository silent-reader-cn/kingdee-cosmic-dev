# 试点单位维护-er_trialorg

## 试点单位维护-多语言表 t_er_trialorg_l

- **表名称：** 试点单位维护-多语言表
- **表名：** t_er_trialorg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_trialorg_l_pkey |  | fpkid |
| 2 | idx_er_trialorg_l_fid |  | fid,flocaleid |

---

## 试点单位明细-子表 t_er_trialorgdetail

- **表名称：** 试点单位明细-子表
- **表名：** t_er_trialorgdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | ftrialorg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_trialorgdetail_pkey |  | fentryid |
| 2 | idx_er_trialorg_fseq |  | fid,fseq |

---

## 试点单位维护-主表 t_er_trialorg

- **表名称：** 试点单位维护-主表
- **表名：** t_er_trialorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | ffunction | 单据/功能 : | varchar | 30 |  | √ | ' ' | 单据/功能 :,枚举: er_tripreqbill :出差申请单 er_loanbill :出差申请单（借） er_tripreimbursebill :差旅报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 printsetting :移动打印 bee_intair :中兴国际机票预订 bee_domair :中兴国内机票预订 bee_hotel :中兴国内酒店预订 bee_train :中兴国内火车预订 bee_car :中兴国内用车预订 corp_intair :携程国际机票预订 corp_domair :携程国内机票预订 corp_inthotel :携程国际酒店预订 corp_hotel :携程国内酒店预订 corp_car :携程用车预订 corp_train :携程火车预订 travelnoone_domair :差旅壹号国内机票预订 travelnoone_hotel :差旅壹号国内酒店预订 travelnoone_car :差旅壹号用车预订 travelnoone_train :差旅壹号火车预订 didi_car :滴滴用车预订 er_dailyvehiclebill :用车申请单 er_checking_exp_list :部门费用清单 er_mealapplication_bill :用餐申请单 meituan_dinner :美团用餐 travelnoone_meal :差旅壹号用餐预订 corp_usergrant :携程员工授权 didi_usergrant :滴滴员工授权 travelnoone_usergrant :差旅壹号员工授权 gaode_car :高德用车预定 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 9 | ftrialstyle | 设置方式 : | varchar | 30 |  | √ | ' ' | 设置方式 :,枚举: 0 :白名单 1 :黑名单 |
| 10 | fstatus | 数据状态 | varchar | 36 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trialorg_fcreateorgid |  | fcreateorgid |
| 2 | t_er_trialorg_pkey |  | fid |
| 3 | idx_er_trialorg_fnumber |  | fnumber |
| 4 | idx_er_trialorg_ffunction |  | ffunction |
