# 部门s-HR同步映射关系-xkbos_adminorg_shr

## 部门s-HR同步映射关系-多语言表 t_xkbas_adminorg_shr_l

- **表名称：** 部门s-HR同步映射关系-多语言表
- **表名：** t_xkbas_adminorg_shr_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshrorgname | 行政组织名称 | varchar | 100 |  | √ | ' ' | 行政组织名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fshrorgfullname | 行政组织全称 | varchar | 500 |  |  | ' ' | 行政组织全称 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_adminorg_shr_l |  | fpkid |
| 2 | idx_adminorg_shr_l_fid |  | fid,flocaleid |

---

## 部门s-HR同步映射关系-主表 t_xkbas_adminorg_shr

- **表名称：** 部门s-HR同步映射关系-主表
- **表名：** t_xkbas_adminorg_shr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshrorgname | 行政组织名称 | varchar | 255 |  | √ | ' ' | 行政组织名称 |
| 3 | fadminorgid | 部门编码 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 4 | fshrorgid | 内码 | varchar | 44 |  | √ | ' ' | 内码 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fshrorgfullname | 行政组织全称 | varchar | 500 |  |  | ' ' | 行政组织全称 |
| 7 | fshrorgnumber | 行政组织编码 | varchar | 80 |  | √ | ' ' | 行政组织编码 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_adminorg_shr_num |  | fshrorgnumber |
| 2 | pk_t_xkbas_adminorg_shr |  | fid |
| 3 | idx_adminorg_shr_id |  | fshrorgid |
| 4 | idx_adminorg_shr_org_id |  | fadminorgid |
