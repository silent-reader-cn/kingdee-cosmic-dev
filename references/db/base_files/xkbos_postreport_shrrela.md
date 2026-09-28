# 岗位汇报关系s-HR同步映射关系-xkbos_postreport_shrrela

## 岗位汇报关系s-HR同步映射关系-主表 t_xksec_postreport_shrrel

- **表名称：** 岗位汇报关系s-HR同步映射关系-主表
- **表名：** t_xksec_postreport_shrrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freportid | 汇报关系 | int8 | 64 |  | √ | 0 | [汇报关系 bos_reportrelation](../base_files/bos_reportrelation.md) |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fparent_shrpostnumber | 上级岗位编码 | varchar | 80 |  | √ | ' ' | 上级岗位编码 |
| 5 | fshrreportid | 内码 | varchar | 50 |  | √ | ' ' | 内码 |
| 6 | fshrpostname | 岗位名称 | varchar | 80 |  | √ | ' ' | 岗位名称 |
| 7 | fshrpostnumber | 岗位编码 | varchar | 80 |  | √ | ' ' | 岗位编码 |
| 8 | fparent_shrpostname | 上级岗位名称 | varchar | 80 |  | √ | ' ' | 上级岗位名称 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xksec_postreport_shrrel |  | fid |
| 2 | idx_xksec_postreport_shrrel_id |  | freportid |

---

## 岗位汇报关系s-HR同步映射关系-多语言表 t_xksec_postreport_shrrel_l

- **表名称：** 岗位汇报关系s-HR同步映射关系-多语言表
- **表名：** t_xksec_postreport_shrrel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fshrpostname | 岗位名称 | varchar | 80 |  | √ | ' ' | 岗位名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fparent_shrpostname | 上级岗位名称 | varchar | 80 |  |  | ' ' | 上级岗位名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xksec_postreport_shrrel__f |  | fid,flocaleid |
| 2 | pk_xksec_postreport_shrrel_l |  | fpkid |
