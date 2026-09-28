# 帮助文档-srm_srmhelp

## 帮助文档-主表 t_pur_srmhelp

- **表名称：** 帮助文档-主表
- **表名：** t_pur_srmhelp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fnecessaryreg | 强制阅读协议 | bpchar | 1 |  | √ | '0' | 强制阅读协议 |
| 8 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 13 | fbiztype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :帮助文档 2 :供应商注册协议 3 :其他 A :专家注册协议 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 16 | fcontent | 内容 | text | 0 |  |  | null | 内容 |
| 17 | fbillno | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_srmhelp_pkey |  | fid |
| 2 | idx_pur_srmhelp_fbillno |  | fbillno |

---

## 帮助文档-多语言表 t_pur_srmhelp_l

- **表名称：** 帮助文档-多语言表
- **表名：** t_pur_srmhelp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_srmhelp_l_pkey |  | fpkid |
| 2 | idx_pur_srmhelp_l_fid |  | fid,flocaleid |
