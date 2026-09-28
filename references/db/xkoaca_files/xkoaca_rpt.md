# 经营报表实体-xkoaca_rpt

## 可用人员-多选基础资料表 t_xkoaca_rptuser

- **表名称：** 可用人员-多选基础资料表
- **表名：** t_xkoaca_rptuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rptuser |  | fpkid |
| 2 | idx_xkoaca_rptuser |  | fid |

---

## 经营报表实体-多语言表 t_xkoaca_rpt_l

- **表名称：** 经营报表实体-多语言表
- **表名：** t_xkoaca_rpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frptname | 报表名称 | varchar | 255 |  | √ | ' ' | 报表名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rpt_l |  | fpkid |
| 2 | idx_xkoaca_rpt_l |  | fid,flocaleid |

---

## 经营报表实体-主表 t_xkoaca_rpt

- **表名称：** 经营报表实体-主表
- **表名：** t_xkoaca_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | ftemplateid | 报表模版 | int8 | 64 |  | √ | 0 | [经营报表模板 xkoaca_rpttemplate](../xkoaca_files/xkoaca_rpttemplate.md) |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'C' |  |
| 5 | fcreatetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 6 | frptname | 报表名称 | varchar | 255 |  | √ | ' ' | 报表名称 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | frowsrcdim | 行维度 | bpchar | 1 |  | √ | ' ' | 行维度,枚举: 1 :经营主体+时间维度 2 :经营指标+时间维度 3 :经营主体+经营指标 4 :经营主体 5 :时间维度 6 :经营指标 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fcolsrcdim | 列维度 | bpchar | 1 |  | √ | ' ' | 列维度,枚举: 1 :经营主体+时间维度 2 :经营指标+时间维度 3 :经营主体+经营指标 4 :经营主体 5 :时间维度 6 :经营指标 |
| 12 | fcreatorid | 发布人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoaca_rpttplid |  | ftemplateid |
| 2 | pk_xkoaca_rpt |  | fid |

---

## 可用角色-多选基础资料表 t_xkoaca_rptrole

- **表名称：** 可用角色-多选基础资料表
- **表名：** t_xkoaca_rptrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoaca_rptrole |  | fpkid |
| 2 | idx_xkoaca_rptrole |  | fid |
