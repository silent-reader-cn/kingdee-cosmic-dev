# 隐私声明-privacystatement

## 隐私声明-多语言表 t_perm_privacystmt_l

- **表名称：** 隐私声明-多语言表
- **表名：** t_perm_privacystmt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fcontent | fcontent | varchar | 2000 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_perm_privacystmt_l_fid |  | fid,flocaleid |
| 2 | t_perm_privacystmt_l_pkey |  | fpkid |

---

## 隐私声明-主表 t_perm_privacystmt

- **表名称：** 隐私声明-主表
- **表名：** t_perm_privacystmt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 6 | flocaleid | 语种 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fcontent | 内容 | text | 0 |  |  | ' ' | 内容 |
| 15 | fversion | 版本 | varchar | 80 |  | √ | ' ' | 版本 |
| 16 | fformid | 业务对象 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_perm_privacystmt_number |  | fnumber |
| 2 | t_perm_privacystmt_pkey |  | fid |
