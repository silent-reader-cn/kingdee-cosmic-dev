# 受控辅助资料类别-bd_ctrlassistdatatype

## 受控辅助资料类别-多语言表 t_bd_ctrlassistdatatype_l

- **表名称：** 受控辅助资料类别-多语言表
- **表名：** t_bd_ctrlassistdatatype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_ctrlassistdatatype_l |  | fpkid |
| 2 | idx_ctrlassistdatatype_l_id |  | fid,flocaleid |

---

## 受控辅助资料类别-主表 t_bd_ctrlassistdatatype

- **表名称：** 受控辅助资料类别-主表
- **表名：** t_bd_ctrlassistdatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 受控辅助资料类别 bd_ctrlassistdatatype |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbizcloudid | 业务云 | varchar | 36 |  |  | ' ' | 业务云 bos_devportal_bizcloud |
| 8 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 9 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 10 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 11 | fispreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fctrlviewid | 控制视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_ctrlassistdatatype |  | fid |
| 2 | idx_ctrlassistdatatype_number |  | fnumber |
