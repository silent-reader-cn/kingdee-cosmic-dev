# 附件字段实体(工具)-bd_attachment_tool

## 附件字段实体(工具)-多语言表 t_bd_attachment_l

- **表名称：** 附件字段实体(工具)-多语言表
- **表名：** t_bd_attachment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 附件名称 | varchar | 255 |  | √ | ' ' | 附件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_attachment_l_fid_flocaleid_key |  | fid,flocaleid |
| 2 | t_bd_attachment_l_pkey |  | fpkid |
| 3 | idx_bd_attachment_l_fid |  | fid,flocaleid |

---

## 附件字段实体(工具)-主表 t_bd_attachment

- **表名称：** 附件字段实体(工具)-主表
- **表名：** t_bd_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 附件名称 | varchar | 255 |  | √ | ' ' | 附件名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | ffilesource | 文件来源 | int4 | 32 |  |  | 0 | 文件来源 |
| 6 | fpreviewurl | 预览地址 | varchar | 500 |  | √ | ' ' | 预览地址 |
| 7 | ftempfile | 临时文件 | bpchar | 1 |  | √ | '0' | 临时文件 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 附件状态 | bpchar | 1 |  | √ | ' ' | 附件状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fpageid | 页面编码 | varchar | 110 |  | √ | ' ' | 页面编码 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftype | 附件类型 | varchar | 30 |  | √ | ' ' | 附件类型 |
| 14 | fdragseq | fdragseq | int8 | 64 |  | √ | 0 |  |
| 15 | fsize | 附件大小 | int8 | 64 |  | √ | 0 | 附件大小 |
| 16 | fsort | 排序字段 | int4 | 32 |  |  | null | 排序字段 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | furl | 附件地址 | varchar | 500 |  | √ | ' ' | 附件地址 |
| 19 | fuid | 附件uid | varchar | 60 |  | √ | ' ' | 附件uid |
| 20 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_attachment_fuid_key |  | fuid |
| 2 | idx_bd_attachment_furl |  | furl |
| 3 | t_bd_attachment_pkey |  | fid |
