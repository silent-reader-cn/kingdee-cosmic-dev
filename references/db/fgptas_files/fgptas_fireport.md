# 财务报告-fgptas_fireport

## 财务报告-多语言表 t_fgptas_fireport_l

- **表名称：** 财务报告-多语言表
- **表名：** t_fgptas_fireport_l

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
| 1 | idx_fgptas_fireport_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_fireport_l |  | fpkid |

---

## 财务报告-主表 t_fgptas_fireport

- **表名称：** 财务报告-主表
- **表名：** t_fgptas_fireport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | freportoutputjson | 报告链接 | varchar | 2000 |  | √ | ' ' | 报告链接 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fparagraphids | 报告章节 | varchar | 1024 |  | √ | ' ' | 报告章节 |
| 8 | freporttemplateid | 报告模板 | int8 | 64 |  | √ | 0 | [财务报告模板 fgptas_fireporttemplate](../fgptas_files/fgptas_fireporttemplate.md) |
| 9 | fgendocumenttype | 生成文档类型 | varchar | 50 |  | √ | ' ' | 生成文档类型,枚举: 1 :Word 2 :PPT |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 11 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fperiod | 期间 | varchar | 1024 |  | √ | ' ' | 期间,枚举: |
| 16 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fcycleid | 周期类型 | varchar | 1024 |  | √ | ' ' | 周期类型,枚举: 2 :日报 4 :月报 5 :季报 6 :半年报 7 :年报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_fireport |  | fid |
| 2 | idx_fgptas_firpt_number |  | fnumber |
