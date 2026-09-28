# 层级知识数据-gai_repo_treedata

## 层级知识数据-分表 t_gai_repo_treedata_d

- **表名称：** 层级知识数据-分表
- **表名：** t_gai_repo_treedata_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatafield06 | 字段06 | varchar | 255 |  | √ | ' ' | 字段06 |
| 3 | fdatafield07 | 字段07 | varchar | 255 |  | √ | ' ' | 字段07 |
| 4 | fdatafield08 | 字段08 | varchar | 255 |  | √ | ' ' | 字段08 |
| 5 | fdatafield09 | 字段09 | varchar | 255 |  | √ | ' ' | 字段09 |
| 6 | fdatafield10_tag | 字段10_详情 | text | 0 |  |  | null | 字段10_详情 |
| 7 | fdatafield15_tag | 字段15_详情 | text | 0 |  |  | null | 字段15_详情 |
| 8 | fdatafield01_tag | 字段01_详情 | text | 0 |  |  | null | 字段01_详情 |
| 9 | fdatafield02_tag | 字段02_详情 | text | 0 |  |  | null | 字段02_详情 |
| 10 | fdatafield19_tag | 字段19_详情 | text | 0 |  |  | null | 字段19_详情 |
| 11 | fdatafield06_tag | 字段06_详情 | text | 0 |  |  | null | 字段06_详情 |
| 12 | fdatafield11_tag | 字段11_详情 | text | 0 |  |  | null | 字段11_详情 |
| 13 | fdatafield16_tag | 字段16_详情 | text | 0 |  |  | null | 字段16_详情 |
| 14 | fdatafield03_tag | 字段03_详情 | text | 0 |  |  | null | 字段03_详情 |
| 15 | fdatafield07_tag | 字段07_详情 | text | 0 |  |  | null | 字段07_详情 |
| 16 | fdatafield20 | 字段20 | varchar | 255 |  | √ | ' ' | 字段20 |
| 17 | fdatafield01 | 字段01 | varchar | 255 |  | √ | ' ' | 字段01 |
| 18 | fdatafield02 | 字段02 | varchar | 255 |  | √ | ' ' | 字段02 |
| 19 | fdatafield03 | 字段03 | varchar | 255 |  | √ | ' ' | 字段03 |
| 20 | fdatafield04 | 字段04 | varchar | 255 |  | √ | ' ' | 字段04 |
| 21 | fdatafield05 | 字段05 | varchar | 255 |  | √ | ' ' | 字段05 |
| 22 | fdatafield20_tag | 字段20_详情 | text | 0 |  |  | null | 字段20_详情 |
| 23 | fdatafield17 | 字段17 | varchar | 255 |  | √ | ' ' | 字段17 |
| 24 | fdatafield18 | 字段18 | varchar | 255 |  | √ | ' ' | 字段18 |
| 25 | fdatafield17_tag | 字段17_详情 | text | 0 |  |  | null | 字段17_详情 |
| 26 | fdatafield19 | 字段19 | varchar | 255 |  | √ | ' ' | 字段19 |
| 27 | fdatafield04_tag | 字段04_详情 | text | 0 |  |  | null | 字段04_详情 |
| 28 | fdatafield12_tag | 字段12_详情 | text | 0 |  |  | null | 字段12_详情 |
| 29 | fdatafield08_tag | 字段08_详情 | text | 0 |  |  | null | 字段08_详情 |
| 30 | fdatafield05_tag | 字段05_详情 | text | 0 |  |  | null | 字段05_详情 |
| 31 | fdatafield13_tag | 字段13_详情 | text | 0 |  |  | null | 字段13_详情 |
| 32 | fdatafield14_tag | 字段14_详情 | text | 0 |  |  | null | 字段14_详情 |
| 33 | fdatafield10 | 字段10 | varchar | 255 |  | √ | ' ' | 字段10 |
| 34 | fdatafield11 | 字段11 | varchar | 255 |  | √ | ' ' | 字段11 |
| 35 | fdatafield12 | 字段12 | varchar | 255 |  | √ | ' ' | 字段12 |
| 36 | fdatafield18_tag | 字段18_详情 | text | 0 |  |  | null | 字段18_详情 |
| 37 | fdatafield13 | 字段13 | varchar | 255 |  | √ | ' ' | 字段13 |
| 38 | fdatafield14 | 字段14 | varchar | 255 |  | √ | ' ' | 字段14 |
| 39 | fdatafield15 | 字段15 | varchar | 255 |  | √ | ' ' | 字段15 |
| 40 | fdatafield09_tag | 字段09_详情 | text | 0 |  |  | null | 字段09_详情 |
| 41 | fdatafield16 | 字段16 | varchar | 255 |  | √ | ' ' | 字段16 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_treedata_d |  | fid |
| 2 | idx_gai_repo_treedata_d_01 |  | fdatafield01 |

---

## 层级知识数据-主表 t_gai_repo_treedata

- **表名称：** 层级知识数据-主表
- **表名：** t_gai_repo_treedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstructrepo | 结构化知识库 | int8 | 64 |  | √ | 0 | [结构化知识库 gai_struct_repo](../gai_files/gai_struct_repo.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fdatastatus | 向量化状态 | varchar | 50 |  | √ | ' ' | 向量化状态,枚举: success :可用 failed :异常 processing :处理中 none :未处理 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ferrormsg | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 17 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [层级知识数据 gai_repo_treedata](../gai_files/gai_repo_treedata.md) |
| 18 | ferrormsgdetail | 失败详细原因 | varchar | 2000 |  | √ | ' ' | 失败详细原因 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_repo_treedata_corg |  | fcreateorgid |
| 2 | idx_gai_repo_treedata_master |  | fmasterid |
| 3 | pk_t_gai_repo_treedata |  | fid |
| 4 | idx_t_gai_repo_treedata_createorg |  | fcreateorgid |
| 5 | idx_t_gai_repo_treedata_master |  | fmasterid |

---

## 层级知识数据-多语言表 t_gai_repo_treedata_l

- **表名称：** 层级知识数据-多语言表
- **表名：** t_gai_repo_treedata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_treedata_l |  | fpkid |
| 2 | idx_gai_repo_treedata_l_0 |  | fid,flocaleid |

---

## 层级知识数据-使用范围表 t_gai_repo_treedata_u

- **表名称：** 层级知识数据-使用范围表
- **表名：** t_gai_repo_treedata_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_treedata_u |  | fdataid,fuseorgid |
| 2 | idx_t_gai_repo_treedata_u_uo |  | fuseorgid |
