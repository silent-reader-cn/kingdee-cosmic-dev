# 数据快照-fcs_datasnap

## 数据快照-多语言表 t_fcs_datasnap_l

- **表名称：** 数据快照-多语言表
- **表名：** t_fcs_datasnap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_datasnap_l |  | fpkid |
| 2 | idx_t_fcs_datasnap_l |  | fid,flocaleid |

---

## 数据快照-主表 t_fcs_datasnap

- **表名称：** 数据快照-主表
- **表名：** t_fcs_datasnap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsnap | 快照 | varchar | 255 |  | √ | ' ' | 快照 |
| 5 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 6 | fcolumns | fcolumns | varchar | 255 |  | √ | ' ' |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fcolumns_tag | fcolumns_tag | text | 0 |  |  | ' ' |  |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsnapdate | 快照日期 | timestamp | 0 |  |  | null | 快照日期 |
| 11 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 12 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 13 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ffields_tag | datasetfields_详情 | text | 0 |  |  | ' ' | datasetfields_详情 |
| 15 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 16 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fsnap_tag | 快照_详情 | text | 0 |  |  | ' ' | 快照_详情 |
| 23 | fformid | 报表 | varchar | 80 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 24 | ffields | datasetfields | varchar | 255 |  | √ | ' ' | datasetfields |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_datasnap |  | forgid,fnumber,fformid |
| 2 | pk_t_fcs_datasnap |  | fid |
