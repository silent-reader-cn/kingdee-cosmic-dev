# 预置表样-xkrpt_sample_presetstyle

## 预置表样-主表 t_xkrpt_presetstyle

- **表名称：** 预置表样-主表
- **表名：** t_xkrpt_presetstyle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 模板分类 | int8 | 64 |  | √ | 0 | [预置表样分组 xkrpt_presetstylegroup](../xkrpt_files/xkrpt_presetstylegroup.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsheetname | 表页名称 | varchar | 255 |  | √ | ' ' | 表页名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffiletype | 文件类型 | varchar | 30 |  | √ | ' ' | 文件类型 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | flocalecode | 语言类型 | varchar | 10 |  | √ | 'zh_CN' | 语言类型 |
| 11 | fsamplesource | 模板来源 | bpchar | 1 |  | √ | '0' | 模板来源,枚举: 0 :金蝶预置 1 :手动上传 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fsamplecontent | 模板文件 | varchar | 255 |  | √ | ' ' | 模板文件 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | freporttype | 报表类型 | bpchar | 10 |  | √ | ' ' | 报表类型,枚举: 3 :普通报表 10 :个别报表 11 :合并报表 13 :工作底稿 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 模板编码 | varchar | 30 |  | √ | ' ' | 模板编码 |
| 20 | fsampletype | 模板类型 | bpchar | 10 |  | √ | ' ' | 模板类型,枚举: 1 :单表页模板 2 :套表模板 |
| 21 | fsamplecontent_tag | 模板文件_详情 | text | 0 |  |  | null | 模板文件_详情 |
| 22 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 23 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_presetstyle_number |  | fnumber |
| 2 | pk_xkrpt_presetstyle |  | fid |

---

## 预置表样-多语言表 t_xkrpt_presetstyle_l

- **表名称：** 预置表样-多语言表
- **表名：** t_xkrpt_presetstyle_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_presetstyle_l |  | fpkid |
| 2 | idx_xkrpt_presetstyle_l_id |  | fid |
