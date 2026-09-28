# 环境保护税税种版本详情-tctb_tax_ver_hjbhs

## 环境保护税税种版本详情-主表 t_tctb_tax_ver_hjbhs

- **表名称：** 环境保护税税种版本详情-主表
- **表名：** t_tctb_tax_ver_hjbhs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcshygc | 从事海洋工程 | bpchar | 1 |  | √ | '0' | 从事海洋工程 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fpollutanttype | 污染物类别 | varchar | 50 |  | √ | ' ' | 污染物类别,枚举: 102 :大气污染物 101 :水污染物 103 :噪声 104 :固体废物 |
| 5 | fshljjzclcs | 生活垃圾集中处理场所 | bpchar | 1 |  | √ | '0' | 生活垃圾集中处理场所 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 8 | fcxwsjzclcs | 城乡污水集中处理场所 | bpchar | 1 |  | √ | '0' | 城乡污水集中处理场所 |
| 9 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 hjbhs :环境保护税 qtsf :其他税费 |
| 10 | fver | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 11 | facsb | 按次申报 | bpchar | 1 |  | √ | '0' | 按次申报 |
| 12 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_ver_hjbhs |  | fid |
| 2 | idx_tctb_hjbhs_org |  | forg,ftaxtype |

---

## 环境保护税版本单据体-子表 t_tctb_tax_ver_hjbhs_e

- **表名称：** 环境保护税版本单据体-子表
- **表名：** t_tctb_tax_ver_hjbhs_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 4 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnumber | 排污许可证编号 | varchar | 200 |  | √ | ' ' | 排污许可证编号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_ver_hjbhs_e_fk |  | fid |
| 2 | pk_tctb_tax_ver_hjbhs_e |  | fentryid |
