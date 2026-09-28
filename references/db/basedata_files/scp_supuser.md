# 协同用户-scp_supuser

## 协同用户-多语言表 t_sec_bizpartneruser_l

- **表名称：** 协同用户-多语言表
- **表名：** t_sec_bizpartneruser_l

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
| 1 | t_sec_bizpartneruser_l_pkey |  | fpkid |
| 2 | idx_t_sec_bizpartneruser_l_fid |  | fid,flocaleid |

---

## 协同用户-分表 t_sec_bizpartneruser_p

- **表名称：** 协同用户-分表
- **表名：** t_sec_bizpartneruser_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisstaff | 客服人员 | bpchar | 1 |  | √ | '0' | 客服人员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_bizpartneruser_p_pkey |  | fid |

---

## 协同用户-主表 t_sec_bizpartneruser

- **表名称：** 协同用户-主表
- **表名：** t_sec_bizpartneruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户信息 bos_usergroup_user |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 9 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fbizpartnertype | 商务伙伴类型 | varchar | 10 |  | √ | ' ' | 商务伙伴类型,枚举: 1 :客户 2 :供应商 |
| 15 | fisadmin | 系统管理员 | bpchar | 1 |  | √ | ' ' | 系统管理员 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fusertype | 用户类型 | varchar | 100 |  | √ | ' ' | 用户类型 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_bizpartneruser_pkey |  | fid |
| 2 | idx_t_sec_bizpartu_bizpartu |  | fuserid,fbizpartnerid |
| 3 | idx_t_sec_bizpartu_orgu |  | forgid,fuserid |
