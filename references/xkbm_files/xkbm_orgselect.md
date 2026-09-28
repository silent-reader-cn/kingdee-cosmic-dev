# 预算组织选择-xkbm_orgselect

## 预算组织选择-多语言表 t_xkbm_orgselect_l

- **表名称：** 预算组织选择-多语言表
- **表名：** t_xkbm_orgselect_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | forgname | 组织名称 | varchar | 255 |  | √ | ' ' | 组织名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_orgselect_l |  | fpkid |
| 2 | idx_xkbm_orgselect_l |  | fid,flocaleid |

---

## 预算组织选择-主表 t_xkbm_orgselect

- **表名称：** 预算组织选择-主表
- **表名：** t_xkbm_orgselect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fparentorgid | 上级组织id | varchar | 255 |  | √ | ' ' | 上级组织id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fownerorgid | 所属组织id | varchar | 255 |  | √ | ' ' | 所属组织id |
| 7 | fbudgetorgid | 预算组织架构id | varchar | 255 |  | √ | ' ' | 预算组织架构id |
| 8 | fdeptorgid | 部门组织id | varchar | 255 |  | √ | ' ' | 部门组织id |
| 9 | forgnumber | 组织编码 | varchar | 255 |  | √ | ' ' | 组织编码 |
| 10 | forgtype | 组织类型 | varchar | 20 |  | √ | ' ' | 组织类型 |
| 11 | fbudgetorg | 预算组织架构 | varchar | 255 |  | √ | ' ' | 预算组织架构 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fownerorg | 所属组织 | varchar | 255 |  | √ | ' ' | 所属组织 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | forgtypeid | 组织类型ID | varchar | 20 |  | √ | ' ' | 组织类型ID |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | forgname | 组织名称 | varchar | 255 |  | √ | ' ' | 组织名称 |
| 21 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 22 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |
| 23 | fparentorg | 上级组织 | varchar | 255 |  | √ | ' ' | 上级组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_orgselect_number |  | fnumber |
| 2 | pk_xkbm_orgselect |  | fid |
