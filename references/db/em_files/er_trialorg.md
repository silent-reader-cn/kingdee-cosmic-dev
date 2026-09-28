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
| 4 | ftrialorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

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
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | ffunction | 单据/功能 | varchar | 30 |  | √ | ' ' | 单据/功能,枚举: er_tripreqbill :出差申请单 er_loanbill :出差申请单（借） er_tripreimbursebill :差旅报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 printsetting :移动打印 er_dailyvehiclebill :用车申请单 er_mealapplication_bill :用餐申请单 er_checking_exp_list :部门费用清单 bee_intair :中兴国际机票预订 bee_domair :中兴国内机票预订 bee_hotel :中兴国内酒店预订 bee_train :中兴国内火车预订 bee_car :中兴国内用车预订 corp_intair :携程国际机票预订 corp_domair :携程国内机票预订 corp_inthotel :携程国际酒店预订 corp_hotel :携程国内酒店预订 corp_car :携程用车预订 corp_train :携程火车预订 corp_usergrant :携程员工授权 corp_home :携程首页 travelnoone_domair :差旅壹号国内机票预订 travelnoone_hotel :差旅壹号国内酒店预订 travelnoone_car :差旅壹号用车预订 travelnoone_train :差旅壹号火车预订 travelnoone_meal :差旅壹号用餐预订 travelnoone_usergrant :差旅壹号员工授权 travelnoone_home :差旅壹号首页 didi_car :滴滴用车预订 didi_usergrant :滴滴员工授权 didi_home :滴滴商旅预订 didi_domhotel :滴滴酒店预订 didi_train :滴滴火车预订 didi_domair :滴滴机票预订 meituan_dinner :美团用餐（废弃） gaode_car :高德用车预定 gaode_usergrant :高德员工授权 dtg_usergrant :同程员工授权 dtg_plane_in :同程国内机票预订 dtg_plane_out :同程国际机票预订 dtg_hotel_in :同程国内酒店预订 dtg_hotel_out :同程国际酒店预订 dtg_train :同程火车预订 dtg_car :同程用车预订 dtg_home :同程首页 ali_usergrant :阿里员工授权 ali_home :阿里首页 ali_plane :阿里机票预订 ali_hotel :阿里酒店预订 ali_train :阿里火车预订 ali_car :阿里用车预订 qicheng_home :企橙首页 qicheng_domair :企橙国内机票预订 qicheng_train :企橙国内火车预订 qicheng_domhotel :企橙国内酒店预订 qicheng_usergrant :企橙员工授权 meiya_home :美亚首页 meiya_plane :美亚机票预订 meiya_hotel :美亚酒店预订 meiya_train :美亚火车预订 meiya_usergrant :美亚员工授权 mt_dinner :美团用餐 mt_usergrant :美团员工授权 fj_usergrant :泛嘉员工授权 fj_home :泛嘉首页 fj_domair :泛嘉国内机票预订 fj_train :泛嘉国内火车预订 fj_domhotel :泛嘉国内酒店预订 fj_car :泛嘉用车预订 er_tripreqbill_inter :全球出差申请单 er_tripreimburse_cardgrid :国内/国际差旅报销单 er_aiinteract :差旅智能体 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 9 | ftrialstyle | 设置方式 | varchar | 30 |  | √ | ' ' | 设置方式,枚举: 0 :白名单 1 :黑名单 |
| 10 | fstatus | 数据状态 | varchar | 36 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 1 | t_er_trialorg_pkey |  | fid |
| 2 | idx_er_trialorg_fcreateorgid |  | fcreateorgid |
| 3 | idx_er_trialorg_fnumber |  | fnumber |
| 4 | idx_er_trialorg_ffunction |  | ffunction |
