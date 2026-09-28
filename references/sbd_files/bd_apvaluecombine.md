# 辅助属性值组合-bd_apvaluecombine

## 属性值组合单据体-子表 t_bd_apcombineentry

- **表名称：** 属性值组合单据体-子表
- **表名：** t_bd_apcombineentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedatanum3 | 基础资料主键3 | int8 | 64 |  | √ | 0 | 基础资料主键3 |
| 3 | fbasedatanum4 | 基础资料主键4 | int8 | 64 |  | √ | 0 | 基础资料主键4 |
| 4 | fauxptynum8 | 辅助资料主键8 | int8 | 64 |  | √ | 0 | 辅助资料主键8 |
| 5 | fbasedatanum1 | 基础资料主键1 | int8 | 64 |  | √ | 0 | 基础资料主键1 |
| 6 | fauxptynum7 | 辅助资料主键7 | int8 | 64 |  | √ | 0 | 辅助资料主键7 |
| 7 | fbasedatanum2 | 基础资料主键2 | int8 | 64 |  | √ | 0 | 基础资料主键2 |
| 8 | fauxptynum6 | 辅助资料主键6 | int8 | 64 |  | √ | 0 | 辅助资料主键6 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fauxptynum5 | 辅助资料主键5 | int8 | 64 |  | √ | 0 | 辅助资料主键5 |
| 11 | fauxptynum4 | 辅助资料主键4 | int8 | 64 |  | √ | 0 | 辅助资料主键4 |
| 12 | fauxptynum3 | 辅助资料主键3 | int8 | 64 |  | √ | 0 | 辅助资料主键3 |
| 13 | fauxptynum2 | 辅助资料主键2 | int8 | 64 |  | √ | 0 | 辅助资料主键2 |
| 14 | fauxptynum1 | 辅助资料主键1 | int8 | 64 |  | √ | 0 | 辅助资料主键1 |
| 15 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 16 | fbasedatanum7 | 基础资料主键7 | int8 | 64 |  | √ | 0 | 基础资料主键7 |
| 17 | fbasedatanum8 | 基础资料主键8 | int8 | 64 |  | √ | 0 | 基础资料主键8 |
| 18 | fbasedatanum5 | 基础资料主键5 | int8 | 64 |  | √ | 0 | 基础资料主键5 |
| 19 | fbasedatanum6 | 基础资料主键6 | int8 | 64 |  | √ | 0 | 基础资料主键6 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_apcombineentry |  | fentryid |
| 2 | idx_bd_apcombineentry_fid |  | fid |

---

## 辅助属性值组合-主表 t_bd_apvaluecombine

- **表名称：** 辅助属性值组合-主表
- **表名：** t_bd_apvaluecombine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fauxptyidlist | 参与组合辅助属性 | varchar | 512 |  | √ | ' ' | 参与组合辅助属性 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_apvaluecombine |  | fid |
| 2 | idx_bd_apvaluecombine_fmaterial |  | fmaterial |
