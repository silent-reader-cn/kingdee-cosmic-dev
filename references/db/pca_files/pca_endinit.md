# 结束初始化-pca_endinit

## 结束初始化-多语言表 t_pca_costaccount_l

- **表名称：** 结束初始化-多语言表
- **表名：** t_pca_costaccount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costaccount_l |  | fpkid |
| 2 | idx_pca_costaccount_l_0 |  | fid,flocaleid |

---

## 结束初始化-主表 t_pca_costaccount

- **表名称：** 结束初始化-主表
- **表名：** t_pca_costaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcalsystemid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 7 | fstartperiod | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 8 | fcalcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 9 | fpolicyid | 会计政策(总账) | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 10 | fisinit | 结束初始化 | bpchar | 1 |  | √ | '0' | 结束初始化 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 17 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 18 | fisusing | 启用 | bpchar | 1 |  | √ | '0' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costacc_num |  | fnumber |
| 2 | idx_pca_costacc_calorg |  | fcalorgid |
| 3 | pk_pca_costaccount |  | fid |
