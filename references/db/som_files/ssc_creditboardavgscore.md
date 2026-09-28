# 信用看板公司平均信用分-ssc_creditboardavgscore

## 信用看板公司平均信用分-多语言表 t_tk_creditboardavgscore_l

- **表名称：** 信用看板公司平均信用分-多语言表
- **表名：** t_tk_creditboardavgscore_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_creditboardavgscore_l |  | fpkid |
| 2 | idx_ssc_creboaavgsco_l_flocid |  | fid,flocaleid |

---

## 信用看板公司平均信用分-主表 t_tk_creditboardavgscore

- **表名称：** 信用看板公司平均信用分-主表
- **表名：** t_tk_creditboardavgscore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | favgscore | 平均信用分 | numeric | 19 | 6 | √ | 0.000000 | 平均信用分 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_creboaavgsco_fsscid |  | fsscid |
| 2 | pk_t_tk_creditboardavgscore |  | fid |
