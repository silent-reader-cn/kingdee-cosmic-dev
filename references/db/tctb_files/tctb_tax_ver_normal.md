# 税种通用版本明细-tctb_tax_ver_normal

## 税种通用版本明细-主表 t_tctb_tax_ver_normal

- **表名称：** 税种通用版本明细-主表
- **表名：** t_tctb_tax_ver_normal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 szys :水资源税 |
| 5 | fver | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_ver_normal |  | fid |
| 2 | idx_tctb_tax_ver_normal |  | forg |

---

## 通用单据体-子表 t_tctb_tax_ver_normal_e

- **表名称：** 通用单据体-子表
- **表名：** t_tctb_tax_ver_normal_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifycontexafter | 修改后 | varchar | 500 |  | √ | ' ' | 修改后 |
| 3 | fmodifycontexttitleysjbs | 修改内容元数据字段标识 | varchar | 100 |  | √ | ' ' | 修改内容元数据字段标识 |
| 4 | fmodifycontexbefore | 修改前 | varchar | 100 |  | √ | ' ' | 修改前 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifycontexttitle | 修改内容 | varchar | 100 |  | √ | ' ' | 修改内容 |
| 7 | fmodifycontexbeforecode | 修改前code（后端使用） | varchar | 100 |  | √ | ' ' | 修改前code（后端使用） |
| 8 | fmodifycontexaftercode | 修改后code（后端使用） | varchar | 100 |  | √ | ' ' | 修改后code（后端使用） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_ver_normal_e_fk |  | fid |
| 2 | pk_tctb_tax_ver_normal_e |  | fentryid |
