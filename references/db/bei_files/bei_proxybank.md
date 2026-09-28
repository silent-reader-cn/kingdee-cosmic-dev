# 代理行-bei_proxybank

## 代理行-主表 t_bei_proxybank

- **表名称：** 代理行-主表
- **表名：** t_bei_proxybank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswiftcode | Swift Code | varchar | 100 |  | √ | ' ' | Swift Code |
| 3 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | faddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fcountryid | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' |  |
| 13 | fbanknameid | 代理行名称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 14 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fproxyacct | 代理行账号 | varchar | 100 |  | √ | ' ' | 代理行账号 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_proxybank |  | fenable |
| 2 | t_bei_proxybank_pkey |  | fid |

---

## 代理行-多语言表 t_bei_proxybank_l

- **表名称：** 代理行-多语言表
- **表名：** t_bei_proxybank_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_proxybank_l |  | fname,fcomment,fid |
| 2 | t_bei_proxybank_l_pkey |  | fpkid |
