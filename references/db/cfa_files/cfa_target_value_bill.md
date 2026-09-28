# 目标值表-cfa_target_value_bill

## 数据存储实体-子表 t_cfa_targetv_detail

- **表名称：** 数据存储实体-子表
- **表名：** t_cfa_targetv_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffebruary | 二月 | numeric | 23 | 10 |  | null | 二月 |
| 3 | fmarch | 三月 | numeric | 23 | 10 |  | null | 三月 |
| 4 | fonequarter | 一季度 | numeric | 23 | 10 |  | null | 一季度 |
| 5 | fannual | 年度值 | numeric | 23 | 10 |  | null | 年度值 |
| 6 | fjune | 六月 | numeric | 23 | 10 |  | null | 六月 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | faugust | 八月 | numeric | 23 | 10 |  | null | 八月 |
| 9 | fdecember | 十二月 | numeric | 23 | 10 |  | null | 十二月 |
| 10 | ftwoquarter | 二季度 | numeric | 23 | 10 |  | null | 二季度 |
| 11 | flasthalfyear | 上半年 | numeric | 23 | 10 |  | null | 上半年 |
| 12 | foctober | 十月 | numeric | 23 | 10 |  | null | 十月 |
| 13 | fseptember | 九月 | numeric | 23 | 10 |  | null | 九月 |
| 14 | fthreequarter | 三季度 | numeric | 23 | 10 |  | null | 三季度 |
| 15 | flowerhalfyear | 下半年 | numeric | 23 | 10 |  | null | 下半年 |
| 16 | fquota | 指标 | int8 | 64 |  | √ | 0 | 指标库 ipo_quota_info |
| 17 | fmay | 五月 | numeric | 23 | 10 |  | null | 五月 |
| 18 | fnovember | 十一月 | numeric | 23 | 10 |  | null | 十一月 |
| 19 | fjuly | 七月 | numeric | 23 | 10 |  | null | 七月 |
| 20 | fjanuary | 一月 | numeric | 23 | 10 |  | null | 一月 |
| 21 | fapril | 四月 | numeric | 23 | 10 |  | null | 四月 |
| 22 | funits | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 0 :% 1 :元 2 :天 3 :次 4 :无 5 :个 6 :元/人 7 :年 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | ffourquarter | 四季度 | numeric | 23 | 10 |  | null | 四季度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_targetv_detail |  | fentryid |
| 2 | idx_cfa_targetv_detail_fk |  | fid |

---

## 目标值表-主表 t_cfa_target_value

- **表名称：** 目标值表-主表
- **表名：** t_cfa_target_value

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fpolicy | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faccountingsys | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsource | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 0 :手工引入 |
| 9 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftargetannual | 数据年度 | int4 | 32 |  | √ | 0 | 数据年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_target_index |  | fbillno |
| 2 | pk_cfa_target_value |  | fid |
