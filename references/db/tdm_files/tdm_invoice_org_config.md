# 发票同步定时组织配置-tdm_invoice_org_config

## 发票同步定时组织配置-主表 t_tdm_invoice_org_config

- **表名称：** 发票同步定时组织配置-主表
- **表名：** t_tdm_invoice_org_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 1 :进项发票 2 :销项发票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_invoice_org_config |  | fdatatype |
| 2 | pk_tdm_invoice_org_config |  | fid |

---

## 同步组织-多选基础资料表 t_tdm_invoice_orgs

- **表名称：** 同步组织-多选基础资料表
- **表名：** t_tdm_invoice_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_invoice_orgs |  | fpkid |
| 2 | idx_tdm_invoice_orgs_fk |  | fid |
