# 研发与高新报表项目-rdem_yfgxbbxm

## 研发与高新报表项目-多语言表 t_rdem_yfgxbbxm_l

- **表名称：** 研发与高新报表项目-多语言表
- **表名：** t_rdem_yfgxbbxm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 报表项目名称 | varchar | 300 |  | √ | ' ' | 报表项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_yfgxbbxm_l |  | fpkid |
| 2 | idx_rdem_yfgxbbxm_l_0 |  | fid,flocaleid |

---

## 研发与高新报表项目-主表 t_rdem_yfgxbbxm

- **表名称：** 研发与高新报表项目-主表
- **表名：** t_rdem_yfgxbbxm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 报表项目名称 | varchar | 200 |  | √ | ' ' | 报表项目名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 11 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 12 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: gxyhmxb :高新优惠明细表 yfjjyhmxb :研发加计优惠明细表 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 报表项目编号 | varchar | 100 |  | √ | ' ' | 报表项目编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_yfgxbbxm |  | fid |
| 2 | idx_rdem_yfgxbbxm_m0 |  | fmasterid |
